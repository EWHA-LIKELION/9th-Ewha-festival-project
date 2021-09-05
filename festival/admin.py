from django.contrib import admin
from .models import *
# Register your models here.

class nursingImages(admin.TabularInline):
    model = nursingImage

class nursingAdmin(admin.ModelAdmin):
    inlines = [nursingImages, ]

admin.site.register(nursingPost, nursingAdmin)
admin.site.register(nursingComment)

class convergenceImages(admin.TabularInline):
    model = convergenceImage
class convergenceAdmin(admin.ModelAdmin):
    inlines = [convergenceImages, ]
admin.site.register(convergencePost, convergenceAdmin)
admin.site.register(convergenceComment)

class businessImages(admin.TabularInline):
    model = businessImage
class businessAdmin(admin.ModelAdmin):
    inlines = [businessImages, ]
admin.site.register(businessPost, businessAdmin)
admin.site.register(businessComment)

class pharmacyImages(admin.TabularInline):
    model = pharmacyImage
class pharmacyAdmin(admin.ModelAdmin):
    inlines = [pharmacyImages, ]
admin.site.register(pharmacyPost, pharmacyAdmin)
admin.site.register(pharmacyComment)

class musicImages(admin.TabularInline):
    model = musicImage
class musicAdmin(admin.ModelAdmin):
    inlines = [musicImages, ]
admin.site.register(musicPost, musicAdmin)
admin.site.register(musicComment)

class eduImages(admin.TabularInline):
    model = eduImage
class eduAdmin(admin.ModelAdmin):
    inlines = [eduImages, ]
admin.site.register(eduTags)
admin.site.register(eduPost, eduAdmin)
admin.site.register(eduComment)

class engineeringImages(admin.TabularInline):
    model = engineeringImage
class engineeringAdmin(admin.ModelAdmin):
    inlines = [engineeringImages, ]
admin.site.register(engineeringPost, engineeringAdmin)
admin.site.register(engineeringComment)

class humanitiesImages(admin.TabularInline):
    model = humanitiesImage
class humanitiesAdmin(admin.ModelAdmin):
    inlines = [humanitiesImages, ]
admin.site.register(humanitiesTags)
admin.site.register(humanitiesPost, humanitiesAdmin)
admin.site.register(humanitiesComment)

class socialImages(admin.TabularInline):
    model =socialImage
class socialAdmin(admin.ModelAdmin):
    inlines = [socialImages, ]

admin.site.register(socialTags)
admin.site.register(socialPost, socialAdmin)
admin.site.register(socialComment)

class naturalImages(admin.TabularInline):
    model =naturalImage
class naturalAdmin(admin.ModelAdmin):
    inlines = [naturalImages, ]

admin.site.register(naturalTags)
admin.site.register(naturalPost, naturalAdmin)
admin.site.register(naturalComment)

class scratonImages(admin.TabularInline):
    model =scratonmage
class scratonAdmin(admin.ModelAdmin):
    inlines = [scratonImages, ]

admin.site.register(scratonTags)
admin.site.register(scratonPost,scratonAdmin)
admin.site.register(scratonComment)

class artImages(admin.TabularInline):
    model =artImage
class artAdmin(admin.ModelAdmin):
    inlines = [artImages, ]
admin.site.register(artTags)
admin.site.register(artPost, artAdmin)
admin.site.register(artComment)

class hokmaImages(admin.TabularInline):
    model =hokmaImage
class hokmaAdmin(admin.ModelAdmin):
    inlines = [hokmaImages, ]
admin.site.register(hokmaPost, hokmaAdmin)
admin.site.register(hokmaComment)


