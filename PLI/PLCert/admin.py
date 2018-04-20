from django.contrib import admin

# Register your models here.
from .models import Question
from .models import Response
from .models import Course
from .models import Module
from .models import Content
from .models import ItemBase
from .models import Text
from .models import File
from .models import Image
from .models import Video

admin.site.register(Question)
admin.site.register(Response)
admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Content)
#admin.site.register(ItemBase) error that this is abstract and thus can't be registered with admin authorization
admin.site.register(Text)
admin.site.register(File)
admin.site.register(Image)
admin.site.register(Video)
