from Titanpy import Titanpy
# --------- ENDPOINT GROUPS --------- #

    # Accounting
accounting_endpoints = [
    'export/inventory-bills',
    'export/invoice-items',
    'export/invoices',
    'export/payments',
    'ap-credits',
    'ap-payments',
    'inventory-bills',
    'invoices',
    'journal-entries',
    'payments',
    'payment-terms',
    'tax-zones',
]
accounting_id_endpoints = [
    'journal-entries-details/',
    'journal-entries-summary/',
    'payment-types/',
]

# CRM
crm_endpoints = [
    'export/bookings',
    'export/customers',
    'export/customers/contacts',
    'export/leads',
    'export/locations',
    'export/locations/contacts',
    'booking-provider-tags',
    'bookings',
    'customers',
    'customers/contacts',
    'leads',
    'locations',
    'locations/contacts',
]
crm_id_endpoints = [
    'booking-provider-tags/',
    '/bookings',
    '/bookings/',
    '/bookings-contacts/',
    'bookings/',
    'bookings-contacts/',
    'customers/',
    'customers-contacts/',
    'customers-notes/',
    'leads/',
    'leads-notes/',
    'locations/',
    'locations-contacts/',
    'locations-notes/',
]

# Dispatch
dispatch_endpoints = [
    'export/appointment-assignments',
    'appointment_assignments',
    'non-job-appointments',
    'teams',
    'technician-shifts',
    'zones',
]
dispatch_id_endpoints = [
    'non-job-appointments/',
    'teams/',
    'technician-shifts/',
    'zones/',
]

# Installed Systems
installed_systems_endpoints = [
    'installed-equipment',
]
installed_systems_id_endpoints = [
    'installed-equipment/',
]

# Forms
forms_endpoints = [
    'forms',
    'submissions',
]

# Inventory
inventory_endpoints = [
    'export/purchase-orders',
    'adjustments',
    'purchase-orders',
    'purchase-order-markups',
    'purchase-order-types',
    'receipts',
    'returns',
    'transfers',
    'trucks',
    'vendors',
    'warehouses',
]
inventory_id_endpoints = [
    'purchase-orders/',
    'purchase-order-markups/',
    'vendors/',
]

# Job Booking
job_booking_endpoints = [
    'call-reasons',
]

# Job Planning and Management
job_planning_endpoints = [
    'export/appointments',
    'export/job-canceled-logs',
    'export/jobs',
    'export/projects',
    'appointments',
    'job-cancel-reasons',
    'job-hold-reasons',
    'jobs',
    'job-types',
    'projects',
    'project-statuses',
    'project-substatuses',
]
job_planning_id_endpoints = [
    'appointments/',
    'jobs-cancel-reasons/',
    'jobs/',
    'jobs-history/',
    'jobs-notes/',
    'job-types/',
    'projects/',
    'projects-notes/',
    'project-statuses/'
    'project-substatuses/',
]

# Reporting
reporting_endpoints = [
    'report-categories',
]
reporting_id_endpoints = [
    'dynamic-value-sets/',
    '/reports',
    '/reports/',
]

# --------- AVAILABLE ENDPOINTS --------- #

available_endpoints = [
]
available_endpoint_groups = [
    accounting_id_endpoints,
    reporting_endpoints,
    reporting_id_endpoints,
    forms_endpoints,
    crm_endpoints,
    crm_id_endpoints,
    dispatch_endpoints,
    dispatch_id_endpoints,
    installed_systems_endpoints,
    installed_systems_id_endpoints,
    inventory_endpoints,
    inventory_id_endpoints,
    job_booking_endpoints,
    job_planning_endpoints,
    job_planning_id_endpoints,
]
for group in available_endpoint_groups:
    available_endpoints.extend(group)


# --------- TEST ENDPOINTS --------- #
tp = Titanpy()
tp.Connect(cred_path="./credentials/servicetitan_credentials.json")
for endpoint in available_endpoints:
    response = tp.Get(endpoint = endpoint, id=1, category='gamer')
    try:
        print(response.status_code)
        print(response.reason)
    except:
        response = tp.Get(endpoint = endpoint, id=1, category='gamer')
        try:
            print(response.status_code)
            print(response.reason)
        except:
            pass