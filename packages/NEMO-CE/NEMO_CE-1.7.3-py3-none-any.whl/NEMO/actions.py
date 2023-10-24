from django.contrib import admin, messages
from django.db.models import Max
from django.urls import reverse
from django.utils.safestring import mark_safe

from NEMO.models import Area, Interlock, InterlockCard, Qualification, Tool, User
from NEMO.typing import QuerySetType
from NEMO.views.access_requests import access_csv_export
from NEMO.views.adjustment_requests import adjustments_csv_export
from NEMO.views.shadowing_verification import shadowing_verification_requests_csv_export


@admin.action(description="Disable selected cards")
def disable_selected_cards(model_admin, request, queryset: QuerySetType[InterlockCard]):
	for interlock_card in queryset:
		interlock_card.enabled = False
		interlock_card.save(update_fields=["enabled"])


@admin.action(description="Enable selected cards")
def enable_selected_cards(model_admin, request, queryset: QuerySetType[InterlockCard]):
	for interlock_card in queryset:
		interlock_card.enabled = True
		interlock_card.save(update_fields=["enabled"])


@admin.action(description="Lock selected interlocks")
def lock_selected_interlocks(model_admin, request, queryset):
	for interlock in queryset:
		try:
			command_succeeded = interlock.lock()
			if command_succeeded:
				messages.success(request, f"{interlock} has been successfully locked")
			else:
				messages.error(request, f"{interlock} could not be locked. {interlock.most_recent_reply}")
		except Exception as error:
			messages.error(request, f"{interlock} could not be locked due to the following error: {str(error)}")


@admin.action(description="Unlock selected interlocks")
def unlock_selected_interlocks(model_admin, request, queryset):
	for interlock in queryset:
		try:
			command_succeeded = interlock.unlock()
			if command_succeeded:
				messages.success(request, f"{interlock} has been successfully unlocked")
			else:
				messages.error(request, f"{interlock} could not be unlocked. {interlock.most_recent_reply}")
		except Exception as error:
			messages.error(request, f"{interlock} could not be unlocked due to the following error: {str(error)}")


@admin.action(description="Synchronize selected interlocks with tool usage")
def synchronize_with_tool_usage(model_admin, request, queryset):
	for interlock in queryset:
		# Ignore interlocks with no tool assigned, and ignore interlocks connected to doors
		if not hasattr(interlock, "tool") or hasattr(interlock, "door"):
			continue
		if interlock.tool.in_use():
			interlock.unlock()
		else:
			interlock.lock()


@admin.action(description="Create next interlock")
def create_next_interlock(model_admin, request, queryset):
	for interlock in queryset:
		new_interlock = Interlock()
		new_interlock.card = interlock.card
		new_interlock.unit_id = interlock.unit_id
		max_channel = Interlock.objects.filter(card=interlock.card).aggregate(Max("channel"))["channel__max"]
		new_interlock.channel = max_channel + 1 if max_channel is not None else None
		new_interlock.save()


@admin.action(description="Duplicate selected tool configuration")
def duplicate_tool_configuration(model_admin, request, queryset):
	for tool in queryset:
		original_name = tool.name
		new_name = "Copy of " + tool.name
		try:
			if Tool.objects.filter(name=new_name).exists():
				messages.error(
					request,
					mark_safe(
						f'There is already a copy of {original_name} as <a href="{reverse("admin:NEMO_tool_change", args=[tool.id])}">{new_name}</a>. Change the copy\'s name and try again'
					),
				)
				continue
			elif tool.is_child_tool():
				messages.warning(request, f"{original_name} is a child tool and cannot be duplicated")
				continue
			else:
				old_required_resources = tool.required_resource_set.all()
				old_nonrequired_resources = tool.nonrequired_resource_set.all()
				old_backup_users = tool.backup_owners.all()
				old_superusers = tool.superusers.all()
				old_reviewers = tool.adjustment_request_reviewers.all()
				old_shadowing_verification_request_qualification_levels = tool.shadowing_verification_request_qualification_levels.all()
				old_id = tool.pk
				tool.pk = None
				tool.interlock = None
				tool.visible = False
				tool.operational = False
				tool.name = new_name
				tool.image = None
				tool.description = None
				tool.serial = None
				tool.save()
				tool.required_resource_set.set(old_required_resources)
				tool.nonrequired_resource_set.set(old_nonrequired_resources)
				tool.backup_owners.set(old_backup_users)
				tool.superusers.set(old_superusers)
				tool.adjustment_request_reviewers.set(old_reviewers)
				tool.shadowing_verification_request_qualification_levels.set(old_shadowing_verification_request_qualification_levels)
				for user in User.objects.filter(qualifications__id=old_id).distinct():
					qualification_level = Qualification.objects.get(user=user, tool__id=old_id).qualification_level
					user.add_qualification(tool, qualification_level)
				messages.success(
					request,
					mark_safe(
						f'A duplicate of {original_name} has been made as <a href="{reverse("admin:NEMO_tool_change", args=[tool.id])}">{tool.name}</a>'
					),
				)
		except Exception as error:
			messages.error(
				request, f"{original_name} could not be duplicated because of the following error: {str(error)}"
			)


@admin.action(description="Rebuild area tree")
def rebuild_area_tree(model_admin, request, queryset):
	Area.objects.rebuild()


@admin.action(description="Export selected adjustment requests in CSV")
def adjustment_requests_export_csv(modeladmin, request, queryset):
	return adjustments_csv_export(queryset.all())


@admin.action(description="Export selected access requests in CSV")
def access_requests_export_csv(modeladmin, request, queryset):
	return access_csv_export(queryset.all())


@admin.action(description="Export selected shadowing verification requests in CSV")
def shadowing_verification_requests_export_csv(modeladmin, request, queryset):
	return shadowing_verification_requests_csv_export(queryset.all())
