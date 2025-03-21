from django.contrib import admin

from subwaive.models import DocusealField,DocusealFieldStore,DocusealSubmission,DocusealSubmitter,DocusealSubmitterSubmission,DocusealTemplate
from subwaive.models import Person,PersonDocuseal,PersonEmail,PersonStripe
from subwaive.models import Log,QRCategory,QRCustom
from subwaive.models import StripePaymentLink,StripePrice,StripeProduct,StripeSubscription,StripeCustomer


"""
Docuseal
"""

class DocusealField_Admin(admin.ModelAdmin):
    list_display = ('field',)
admin.site.register(DocusealField, DocusealField_Admin)

class DocusealFieldStore_Admin(admin.ModelAdmin):
    list_display = ('submission', 'field', 'value',)
admin.site.register(DocusealFieldStore, DocusealFieldStore_Admin)

class DocusealSubmission_Admin(admin.ModelAdmin):
    list_display = ('submission_id', 'slug', 'status', 'completed_at', 'template',)
admin.site.register(DocusealSubmission, DocusealSubmission_Admin)

class DocusealSubmitter_Admin(admin.ModelAdmin):
    list_display = ('submitter_id', 'email', 'slug',)
admin.site.register(DocusealSubmitter, DocusealSubmitter_Admin)

class DocusealSubmitterSubmission_Admin(admin.ModelAdmin):
    list_display = ('submitter', 'submission',)
admin.site.register(DocusealSubmitterSubmission, DocusealSubmitterSubmission_Admin)

class DocusealTemplate_Admin(admin.ModelAdmin):
    list_display = ('template_id', 'folder_name', 'name', 'slug',)
admin.site.register(DocusealTemplate, DocusealTemplate_Admin)


"""
Person
"""

class Person_Admin(admin.ModelAdmin):
    list_display = ('name', 'preferred_email',)
admin.site.register(Person, Person_Admin)

class PersonDocuseal_Admin(admin.ModelAdmin):
    list_display = ('person', 'submitter_id',)
admin.site.register(PersonDocuseal, PersonDocuseal_Admin)

class PersonEmail_Admin(admin.ModelAdmin):
    list_display = ('person', 'email',)
admin.site.register(PersonEmail, PersonEmail_Admin)

class PersonStripe_Admin(admin.ModelAdmin):
    list_display = ('person', 'customer_id',)
admin.site.register(PersonStripe, PersonStripe_Admin)


"""
Other
"""

class Log_Admin(admin.ModelAdmin):
    list_display = ('timestamp', 'description',)
admin.site.register(Log, Log_Admin)

class QRCategory_Admin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(QRCategory, QRCategory_Admin)

class QRCustom_Admin(admin.ModelAdmin):
    list_display = ('category', 'name',)
admin.site.register(QRCustom, QRCustom_Admin)


"""
Stripe
"""

class StripeCustomer_Admin(admin.ModelAdmin):
    list_display = ('stripe_id', 'name',)
admin.site.register(StripeCustomer, StripeCustomer_Admin)

class StripePaymentLink_Admin(admin.ModelAdmin):
    list_display = ('stripe_id', 'url',)
admin.site.register(StripePaymentLink, StripePaymentLink_Admin)

class StripePrice_Admin(admin.ModelAdmin):
    list_display = ('stripe_id', 'interval', 'price',)
admin.site.register(StripePrice, StripePrice_Admin)

class StripeProduct_Admin(admin.ModelAdmin):
    list_display = ('stripe_id', 'name', 'description',)
admin.site.register(StripeProduct, StripeProduct_Admin)

class StripeSubscription_Admin(admin.ModelAdmin):
    list_display = ('stripe_id', 'customer', 'status', 'created', 'current_period_end',)
admin.site.register(StripeSubscription, StripeSubscription_Admin)