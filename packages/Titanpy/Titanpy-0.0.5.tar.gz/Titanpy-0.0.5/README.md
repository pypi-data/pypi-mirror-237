# Titanpy

Test to practice creating classes as packages in Pypi

Python class for interacting with all Servicetitan's api endpoints

Windows install:
py -m pip install --upgrade Titanpy


## Tutorials:

### Adding get endpoints

First add an endpoint to an endpoint group. This is accomplished by either adding to an existing group or creating a new one. For example, I want to add an exports endpoint for activity-codes. First I would go to the Payroll endpoint group, pick whether I want to add an ID/category endpoint or a normal endpoint. Since the export endpoint does not require an ID, I would add it to the latter. The naming scheme goes as follow:

> {first part of url}-{second part of url}{/ if id, no / if not id}

For the example: 'export/activity-codes'
For an id endpoint from activity-codes: 'activity-codes/'

This was done this way because for more complicated endpoints, they must has specific url formats that can be generated in the handlers/endpoint tests section. However, simple endpoints such as export activity-codes can simply be the format they would be in the url. The slash is added for simple id endpoints because they can simply be in the format {endpoint}/{id}.

Next the endpoint must be added to the available endpoints group list, most of the endpoint groups are already added but if a new group is made feel free to add it. Endpoint group names can be found at [Servicetitan Developer Apis](https://developer.servicetitan.io/apis/) and are based entirely off servicetitan's naming scheme.

The last step before creating a handler/endpoint test is adding the general url if it hasn't already. Please use the following structure when adding to this dictionary:

> "{endpoint group name}_url{_tenant if tenant included}": f"{url(with tenant inserted in the f-string if needed)}",

For more guidance use context clues with the previous general urls.

Finally, you can add the handler/endpoint test.

This section is split up based on endpoint groups with comments designating each endpoint group. You will find most have a handler for id endpoints and standard groups, with id groups being split between simple first then complicated following. Most of these can be copy pasted and then have specific parts replaced based on the current endpoint you are trying to integrate. Please study the general formatting and follow according, they are mostly the same.

And you're done! You've added a get endpoint. Send a pull request to the main branch and it'll be added after a short review.