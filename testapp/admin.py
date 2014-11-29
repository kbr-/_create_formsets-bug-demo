from django.contrib import admin
from testapp import models


class RelatedToGoodModelInline(admin.TabularInline):
	model = models.RelatedToGoodModel
	fields = ['name']

	def get_fieldsets(self, request, obj=None):
		print("RelatedToGoodModelInline.get_fieldsets, obj =", obj)
		return super(RelatedToGoodModelInline, self).get_fieldsets(request, obj)


class GoodModelAdmin(admin.ModelAdmin):
	fields = ['name']
	inlines = [RelatedToGoodModelInline]

	def get_formsets_with_inlines(self, request, obj=None):
		print("GoodModelAdmin.get_formsets_with_inlines, obj =", obj)
		return super(GoodModelAdmin, self).get_formsets_with_inlines(request, obj)
		# for inline in self.get_inline_instances(request, obj):
		# 	if isinstance(inline, RelatedToGoodModelInline) and obj is None:
		# 		continue
		# 	yield inline.get_formset(request, obj), inline


class RelatedToBadModelInline(admin.TabularInline):
	model = models.RelatedToBadModel
	fields = ['name']

	def get_fieldsets(self, request, obj=None):
		print("RelatedToBadModelInline.get_fieldsets, obj =", obj)
		return super(RelatedToBadModelInline, self).get_fieldsets(request, obj)


class BadModelAdmin(admin.ModelAdmin):
	fields = ['id']
	inlines = [RelatedToBadModelInline]

	def get_formsets_with_inlines(self, request, obj=None):
		print("BadModelAdmin.get_formsets_with_inlines, obj =", obj)
		return super(BadModelAdmin, self).get_formsets_with_inlines(request, obj)
		# for inline in self.get_inline_instances(request, obj):
		# 	if isinstance(inline, RelatedToBadModelInline) and obj is None:
		# 		continue
		# 	yield inline.get_formset(request, obj), inline


admin.site.register(models.GoodModel, GoodModelAdmin)
admin.site.register(models.BadModel, BadModelAdmin)