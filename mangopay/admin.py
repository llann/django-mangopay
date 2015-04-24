# -*- coding: UTF-8 -*-

from django.contrib import admin
from mangopay.models import MangoPayUser, MangoPayDocument, MangoPayPage, MangoPayBankAccount, MangoPayWallet, MangoPayTransfer, MangoPayRefund, MangoPayPayIn, MangoPayPayInBankWire, MangoPayCardRegistration, MangoPayCard, MangoPayPayOut, MangoPayBankAccount, MangoPayPage, MangoPayDocument, MangoPayWallet


class MangoPayUserAdmin(admin.ModelAdmin):

    list_display = ('mangopay_id', 'user', 'type', 'first_name', 'last_name', 'country_of_residence',)
admin.site.register(MangoPayUser, MangoPayUserAdmin)


class MangoPayWalletAdmin(admin.ModelAdmin):

    list_display = ('mangopay_id', 'mangopay_user', 'currency',)

admin.site.register(MangoPayWallet, MangoPayWalletAdmin)


class MangoPayDocumentAdmin(admin.ModelAdmin):

    list_display = ('mangopay_id', 'mangopay_user', 'status')

admin.site.register(MangoPayDocument, MangoPayDocumentAdmin)


class MangoPayPageAdmin(admin.ModelAdmin):

    list_display = ('document',)

admin.site.register(MangoPayPage, MangoPayPageAdmin)


class MangoPayBankAccountAdmin(admin.ModelAdmin):

    list_display = ('mangopay_id',)

admin.site.register(MangoPayBankAccount, MangoPayBankAccountAdmin)


class MangoPayPayOutAdmin(admin.ModelAdmin):

    list_display = ('mangopay_id', 'mangopay_user', 'mangopay_wallet', 'status')

admin.site.register(MangoPayPayOut, MangoPayPayOutAdmin)


class MangoPayCardAdmin(admin.ModelAdmin):

    list_display = ('mangopay_id', 'is_active', 'is_valid',)

admin.site.register(MangoPayCard, MangoPayCardAdmin)


class MangoPayCardRegistrationAdmin(admin.ModelAdmin):

    list_display = ('mangopay_id', 'mangopay_user', 'mangopay_card',)

admin.site.register(MangoPayCardRegistration, MangoPayCardRegistrationAdmin)


class MangoPayPayInAdmin(admin.ModelAdmin):

    list_display = ('mangopay_id', 'mangopay_user', 'mangopay_wallet', 'mangopay_card', 'status', )

admin.site.register(MangoPayPayIn, MangoPayPayInAdmin)


class MangoPayPayInBankWireAdmin(admin.ModelAdmin):

    list_display = ('mangopay_id', 'mangopay_user', 'mangopay_wallet', 'execution_date', 'status', 'result_code')

admin.site.register(MangoPayPayInBankWire, MangoPayPayInBankWireAdmin)


class MangoPayRefundAdmin(admin.ModelAdmin):

    list_display = ('mangopay_id', 'mangopay_user', 'mangopay_pay_in', 'execution_date', 'status', )

admin.site.register(MangoPayRefund, MangoPayRefundAdmin)


class MangoPayTransferAdmin(admin.ModelAdmin):

    list_display = ('mangopay_id', 'mangopay_debited_wallet', 'mangopay_credited_wallet', 'debited_funds', 'execution_date', 'status',)

admin.site.register(MangoPayTransfer, MangoPayTransferAdmin)
