from django.urls import include, path
from django.shortcuts import redirect

from staff.views import core

app_name = 'staff'
urlpatterns = [
    path('', lambda r: redirect('staff:tasks:todo'), name="home"),

    # A url file for every tab
    path('tasks/', include('staff.urls.tasks', namespace="tasks")),
    path('members/', include('staff.urls.members', namespace="members")),
    path('activity/', include('staff.urls.activity', namespace="activity")),
    path('billing/', include('staff.urls.billing', namespace="billing")),
    path('stats/', include('staff.urls.stats', namespace="stats")),
    # Logs == Arpwatch
    # Lists == Interlink
    # Doors = Doors
    path('settings/', include('staff.urls.settings', namespace="settings")),

    # Other URLS
    path('event/create/', core.create_event, name='create_event'),
]

# Copyright 2018 Office Nomads LLC (http://www.officenomads.com/) Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
