## progresserpnext

ERPNext Customizations for Progress Software Development GmbH

## Installation

Create a new ERPNext site, if you don't have one yet:

```bash
bench new-site erp.example.org --install-app erpnext
```

Install this app:

```bash
bench --site erp.example.org install-app progresserpnext --branch version-15
```

## Features

- This app comes with a number of custom fields which are defined in the `progresserpnext/custom_fields.py` file.
- The `progresserpnext/dry_run.py` file contains a method to dry-run a document.

    <details>
    <summary>Dry-run API</summary>

    The `progresserpnext.api.dry_run` method can be used to dry-run an action on a document. It takes two parameters:

    - `action`: The action to dry-run [`save`, `submit`, `cancel`].
    - `doc`: The document to dry-run the action on.

    The method returns the document with the action applied.

    Example request:

    ```bash
    curl --location 'http://127.0.0.1:8006/api/v2/method/progresserpnext.api.dry_run' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Basic YThkZDZkMzU2ZjkwYjIwOjlkNzM4ODY3MDIzYjU1MQ==' \
    --data '{
        "action": "save",
        "doc": {
            "naming_series": "ACC-SINV-.YYYY.-",
            "customer": "Max Muster",
            "customer_name": "Max Muster",
            "company": "PSD",
            "currency": "EUR",
            "selling_price_list": "Standard Selling",
            "price_list_currency": "EUR",
            "taxes_and_charges": "Italy VAT 22% - P",
            "customer_address": "Max Muster-Billing",
            "company_address": "PSD-Billing",
            "debit_to": "1310 - Debtors - P",
            "party_account_currency": "EUR",
            "is_opening": "No",
            "against_income_account": "4110 - Sales - P",
            "company_fiscal_code": "12345",
            "company_fiscal_regime": "RF01-Ordinario",
            "customer_fiscal_code": "23456",
            "doctype": "Sales Invoice",
            "items": [
                {
                    "idx": 1,
                    "has_item_scanned": 0,
                    "item_code": "Schachtringe",
                    "custom_parent_line_idx": 0,
                    "custom_is_inclusive": 0,
                    "custom_building": "A",
                    "custom_section": "B",
                    "description": "Schachtringe",
                    "qty": 1.0,
                    "uom": "Nos",
                    "is_free_item": 0,
                    "cost_center": "Main - P"
                }
            ]
        }
    }'
    ```

    Example response:

    ```json
    {
        "data": {
            "name": "ACC-SINV-2025-00002",
            "owner": "Administrator",
            "creation": "2025-02-17 15:40:42.864460",
            "modified": "2025-02-17 15:40:42.864460",
            "modified_by": "Administrator",
            "docstatus": 0,
            "idx": 0,
            "title": "Max Muster",
            "naming_series": "ACC-SINV-.YYYY.-",
            "customer": "Max Muster",
            "customer_name": "Max Muster",
            "tax_id": null,
            "company": "PSD",
            "company_tax_id": "IT123456789",
            "custom_sales_order": null,
            "posting_date": "2025-02-17",
            "posting_time": "15:40:43.043826",
            "set_posting_time": 0,
            "due_date": "2025-02-17",
            "is_pos": 0,
            "pos_profile": null,
            "is_consolidated": 0,
            "is_return": 0,
            "return_against": null,
            "update_outstanding_for_self": 1,
            "update_billed_amount_in_sales_order": 0,
            "update_billed_amount_in_delivery_note": 1,
            "is_debit_note": 0,
            "amended_from": null,
            "cost_center": null,
            "project": null,
            "currency": "EUR",
            "conversion_rate": 1.0,
            "selling_price_list": "Standard Selling",
            "price_list_currency": "EUR",
            "plc_conversion_rate": 1.0,
            "ignore_pricing_rule": 0,
            "scan_barcode": null,
            "update_stock": 0,
            "set_warehouse": null,
            "set_target_warehouse": null,
            "total_qty": 1.0,
            "total_net_weight": 0.0,
            "base_total": 100.0,
            "base_net_total": 100.0,
            "total": 100.0,
            "net_total": 100.0,
            "tax_category": "",
            "taxes_and_charges": "Italy VAT 22% - P",
            "vat_collectability": "I-Immediata",
            "shipping_rule": null,
            "incoterm": null,
            "named_place": null,
            "base_total_taxes_and_charges": 0.0,
            "total_taxes_and_charges": 0.0,
            "base_grand_total": 100.0,
            "base_rounding_adjustment": 0.0,
            "base_rounded_total": 100.0,
            "base_in_words": "EUR One Hundred only.",
            "grand_total": 100.0,
            "rounding_adjustment": 0.0,
            "use_company_roundoff_cost_center": 0,
            "rounded_total": 100.0,
            "in_words": "EUR One Hundred only.",
            "total_advance": 0.0,
            "outstanding_amount": 100.0,
            "disable_rounded_total": 0,
            "apply_discount_on": "Grand Total",
            "base_discount_amount": 0.0,
            "is_cash_or_non_trade_discount": 0,
            "additional_discount_account": null,
            "additional_discount_percentage": 0.0,
            "discount_amount": 0.0,
            "other_charges_calculation": null,
            "total_billing_hours": 0.0,
            "total_billing_amount": 0.0,
            "cash_bank_account": null,
            "base_paid_amount": 0.0,
            "paid_amount": 0.0,
            "base_change_amount": 0.0,
            "change_amount": 0.0,
            "account_for_change_amount": null,
            "allocate_advances_automatically": 0,
            "only_include_allocated_payments": 0,
            "write_off_amount": 0.0,
            "base_write_off_amount": 0.0,
            "write_off_outstanding_amount_automatically": 0,
            "write_off_account": null,
            "write_off_cost_center": null,
            "redeem_loyalty_points": 0,
            "loyalty_points": 0,
            "loyalty_amount": 0.0,
            "loyalty_program": null,
            "loyalty_redemption_account": null,
            "loyalty_redemption_cost_center": null,
            "customer_address": "Max Muster-Billing",
            "address_display": "Julius-Durst-Str. 99<br>\nBrixen<br>\n39042<br>Italy<br>\n<br>\n",
            "contact_person": null,
            "contact_display": null,
            "contact_mobile": null,
            "contact_email": null,
            "territory": null,
            "shipping_address_name": null,
            "shipping_address": null,
            "dispatch_address_name": null,
            "dispatch_address": null,
            "company_address": "PSD-Billing",
            "company_address_display": "Julius-Durst-Str. 100<br>\nBrixen<br>\n39042<br>Italy<br>\n<br>\n",
            "company_contact_person": null,
            "ignore_default_payment_terms_template": 0,
            "payment_terms_template": null,
            "tc_name": null,
            "terms": null,
            "po_no": "",
            "po_date": null,
            "debit_to": "1310 - Debtors - P",
            "party_account_currency": "EUR",
            "is_opening": "No",
            "unrealized_profit_loss_account": null,
            "against_income_account": "4110 - Sales - P",
            "company_fiscal_code": "12345",
            "company_fiscal_regime": "RF01-Ordinario",
            "customer_fiscal_code": "23456",
            "type_of_document": "",
            "sales_partner": null,
            "amount_eligible_for_commission": 100.0,
            "commission_rate": 0.0,
            "total_commission": 0.0,
            "letter_head": null,
            "group_same_items": 0,
            "select_print_heading": null,
            "language": "en",
            "subscription": null,
            "from_date": null,
            "auto_repeat": null,
            "to_date": null,
            "status": "Draft",
            "inter_company_invoice_reference": null,
            "campaign": null,
            "represents_company": null,
            "source": null,
            "customer_group": null,
            "is_internal_customer": 0,
            "is_discounted": 0,
            "remarks": null,
            "doctype": "Sales Invoice",
            "payments": [],
            "items": [
                {
                    "name": "10k754g3tm",
                    "owner": "Administrator",
                    "creation": "2025-02-17 15:40:42.864460",
                    "modified": "2025-02-17 15:40:42.864460",
                    "modified_by": "Administrator",
                    "docstatus": 0,
                    "idx": 1,
                    "barcode": null,
                    "has_item_scanned": 0,
                    "item_code": "Schachtringe",
                    "item_name": "Schachtringe",
                    "custom_parent_line_idx": 0,
                    "custom_is_inclusive": 0,
                    "custom_building": "A",
                    "custom_section": "B",
                    "customer_item_code": null,
                    "description": "Schachtringe",
                    "tax_rate": 0.0,
                    "tax_amount": 0.0,
                    "total_amount": 0.0,
                    "item_group": "Products",
                    "brand": null,
                    "image": "",
                    "customer_po_no": null,
                    "customer_po_date": null,
                    "qty": 1.0,
                    "stock_uom": "Nos",
                    "uom": "Nos",
                    "conversion_factor": 1.0,
                    "stock_qty": 1.0,
                    "price_list_rate": 100.0,
                    "base_price_list_rate": 100.0,
                    "margin_type": "",
                    "margin_rate_or_amount": 0.0,
                    "rate_with_margin": 0.0,
                    "discount_percentage": 0.0,
                    "discount_amount": 0.0,
                    "base_rate_with_margin": 0.0,
                    "rate": 100.0,
                    "amount": 100.0,
                    "item_tax_template": null,
                    "base_rate": 100.0,
                    "base_amount": 100.0,
                    "pricing_rules": null,
                    "stock_uom_rate": 100.0,
                    "is_free_item": 0,
                    "grant_commission": 1,
                    "net_rate": 100.0,
                    "net_amount": 100.0,
                    "base_net_rate": 100.0,
                    "base_net_amount": 100.0,
                    "delivered_by_supplier": 0,
                    "income_account": "4110 - Sales - P",
                    "is_fixed_asset": 0,
                    "asset": null,
                    "finance_book": null,
                    "expense_account": "5111 - Cost of Goods Sold - P",
                    "discount_account": null,
                    "deferred_revenue_account": null,
                    "service_stop_date": null,
                    "enable_deferred_revenue": 0,
                    "service_start_date": null,
                    "service_end_date": null,
                    "weight_per_unit": 0.0,
                    "total_weight": 0.0,
                    "weight_uom": null,
                    "warehouse": "Stores - P",
                    "target_warehouse": null,
                    "quality_inspection": null,
                    "serial_and_batch_bundle": null,
                    "use_serial_batch_fields": 0,
                    "allow_zero_valuation_rate": 0,
                    "incoming_rate": 0.0,
                    "item_tax_rate": "{}",
                    "actual_batch_qty": 0.0,
                    "serial_no": null,
                    "batch_no": null,
                    "actual_qty": 0.0,
                    "company_total_stock": 0.0,
                    "sales_order": null,
                    "so_detail": null,
                    "sales_invoice_item": null,
                    "delivery_note": null,
                    "dn_detail": null,
                    "delivered_qty": 0.0,
                    "purchase_order": null,
                    "purchase_order_item": null,
                    "cost_center": "Main - P",
                    "project": null,
                    "page_break": 0,
                    "parent": "ACC-SINV-2025-00002",
                    "parentfield": "items",
                    "parenttype": "Sales Invoice",
                    "doctype": "Sales Invoice Item"
                }
            ],
            "packed_items": [],
            "advances": [],
            "pricing_rules": [],
            "payment_schedule": [
                {
                    "name": "99dfga9sl3",
                    "owner": "Administrator",
                    "creation": "2025-02-17 15:40:43.102072",
                    "modified": "2025-02-17 15:40:43.102072",
                    "modified_by": "Administrator",
                    "docstatus": 0,
                    "idx": 1,
                    "payment_term": null,
                    "description": null,
                    "due_date": "2025-02-17",
                    "mode_of_payment": null,
                    "mode_of_payment_code": null,
                    "bank_account": null,
                    "bank_account_name": null,
                    "bank_account_no": null,
                    "bank_account_iban": null,
                    "bank_account_swift_number": null,
                    "invoice_portion": 100.0,
                    "discount_type": null,
                    "discount_date": null,
                    "discount": 0.0,
                    "payment_amount": 100.0,
                    "outstanding": 100.0,
                    "paid_amount": 0.0,
                    "discounted_amount": 0.0,
                    "base_payment_amount": 100.0,
                    "parent": "ACC-SINV-2025-00002",
                    "parentfield": "payment_schedule",
                    "parenttype": "Sales Invoice",
                    "doctype": "Payment Schedule"
                }
            ],
            "sales_team": [],
            "taxes": [
                {
                    "name": "u33gomfjof",
                    "owner": "Administrator",
                    "creation": "2025-02-17 15:40:43.101319",
                    "modified": "2025-02-17 15:40:43.101319",
                    "modified_by": "Administrator",
                    "docstatus": 0,
                    "idx": 1,
                    "charge_type": "On Net Total",
                    "row_id": null,
                    "account_head": "IVA 22% - P",
                    "description": "IVA 22% @ 22.0",
                    "included_in_print_rate": 0,
                    "tax_exemption_reason": "",
                    "tax_exemption_law": null,
                    "included_in_paid_amount": 0,
                    "cost_center": "Main - P",
                    "rate": 22.0,
                    "account_currency": null,
                    "tax_amount": 0.0,
                    "total": 0.0,
                    "tax_amount_after_discount_amount": 0.0,
                    "base_tax_amount": 0.0,
                    "base_total": 0.0,
                    "base_tax_amount_after_discount_amount": 0.0,
                    "item_wise_tax_detail": null,
                    "dont_recompute_tax": 0,
                    "parent": "ACC-SINV-2025-00002",
                    "parentfield": "taxes",
                    "parenttype": "Sales Invoice",
                    "doctype": "Sales Taxes and Charges"
                }
            ],
            "timesheets": []
        }
    }
    ```

    </details>

## Contributing

### Update translations

Translations live in the `progresserpnext/locale` directory. The file `main.pot` holds all translatable strings. The `<locale>.po` files hold the actual translations.

To update the `main.pot` file, adding new translatable strings and removing old ones, run:

```bash
bench generate-pot-file --app progresserpnext
```

To sync the locale files with the `main.pot` file, run:

```bash
bench update-po-files --app progresserpnext
```

Add translations by editing the `msgstr` fields in the `<locale>.po` files.

#### License

gpl-3.0
