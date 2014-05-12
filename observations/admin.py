from django.contrib import admin
from observations.models import Observation

class ObservationAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['species']}),
        (None,               {'fields': ['family']}),
        ('Published Date',   {'fields': ['timestamp']}),
        ('Observation Type', {'fields': ['observation_type']}),
        ('Location',         {'fields': ['location']}),
        ('GPS',              {'fields': ['gps']}),    
        ('Lifeform', 	     {'fields': ['lifeform']}),
        ('Phenology', 	     {'fields': ['phenology']}),
        ('Habitat', 	     {'fields': ['habitat']}),
        ('On Serpentine', 	 {'fields': ['onserpentine']}),
        ('Number of Plants', {'fields': ['numplants']}),
        ('Image',            {'fields': ['image']}),
        ('Description',      {'fields': ['description'], 'classes': ['grp-collapse grp-open']}),
        ('Revision Notes',   {'fields': ['revision_notes'], 'classes': ['grp-collapse grp-closed']}),
        ('Observer Name', 	 {'fields': ['observername']}),
        ('Device Name', 	 {'fields': ['devicename']}),
        ('Edited by',        {'fields': ['edited_by']}),
        ('Edited on',        {'fields': ['edited_on']}),
        ('Uploaded',         {'fields': ['uploaded']}),
        ('Validated',        {'fields': ['validated']}),
    ]
    readonly_fields=('timestamp', 'edited_by', 'edited_on')
    list_display = ('species', 'validated', 'uploaded', 'edited_by', 'edited_on', 'family', 'location', 'timestamp', 'observername', 'devicename', 'was_published_recently')
    list_filter = ('validated', 'uploaded', 'timestamp', 'edited_on', 'edited_by', 'family', 'location', 'observation_type', 'onserpentine', 'observername', 'devicename')
    search_fields = ('species', 'family', 'timestamp', 'location', 'lifeform', 'phenology', 'habitat', 'observation_type', 'observername', 'devicename', 'edited_by', 'edited_on')
    date_hierarchy = 'timestamp'
    ordering = ['species']

    def save_model(self, request, obj, form, change):
        obj.edited_by = request.user
        obj.save()

admin.site.register(Observation, ObservationAdmin)
