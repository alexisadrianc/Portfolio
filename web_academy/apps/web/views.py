import random
from django.template.loader import render_to_string
from django.shortcuts import *
from django.views.generic import *
from django.core.mail import EmailMessage
from django.conf import settings
from .models import *
from .forms import *


# Create your views here.
def consult_teacher(id):
    try:
        return Teacher.objects.get(id=id)
    except:
        return None


def consult_lesson(id):
    try:
        return Lesson.objects.get(id=id)
    except:
        return None


def getSocial():
    try:
        return Social.objects.filter(state=True).latest('create_to')
    except:
        return None


def getAbouts():
    try:
        return AboutUs.objects.filter(state=True).latest('create_to')
    except:
        return None


def getExternalLinks():
    try:
        return ExternalServices.objects.filter(state=True).latest('create_to')
    except:
        return None


class Index(ListView):

    def get(self, request, *args, **kwargs):
        teacher = list(Teacher.objects.filter(state=True).values_list('id', flat=True))
        lesson = list(Lesson.objects.filter(state=True).values_list('id', flat=True))
        teacher1 = random.choice(teacher)
        teacher.remove(teacher1)
        teacher2 = random.choice(teacher)
        teacher.remove(teacher2)
        teacher3 = random.choice(teacher)
        teacher.remove(teacher3)
        lesson1 = random.choice(lesson)
        lesson.remove(lesson1)
        lesson2 = random.choice(lesson)
        lesson.remove(lesson2)
        lesson3 = random.choice(lesson)
        lesson.remove(lesson3)

        try:
            post = list(Post.objects.filter(state=True, published=True).values_list('id', flat=True))
            posted = random.choice(post)
            post.remove(posted)
            posted = Post.objects.get(id=posted)
        except:
            posted = None

        context = {
            'post': posted,
            'teacher1': consult_teacher(teacher1),
            'teacher2': consult_teacher(teacher2),
            'teacher3': consult_teacher(teacher3),
            'lesson1': consult_lesson(lesson1),
            'lesson2': consult_lesson(lesson2),
            'lesson3': consult_lesson(lesson3),
            'social': getSocial(),
            'about': getAbouts(),
            'link': getExternalLinks(),
        }
        return render(request, "index.html", context)


class About(ListView):

    def get(self, request, *args, **kwargs):
        try:
            about = AboutUs.objects.filter(state=True)
        except:
            about = None
        try:
            testimonio = Testimonial.objects.filter(state=True, published=True)
        except:
            testimonio = None

        context = {
            'about_us': about,
            'testimonio': testimonio,
            'social': getSocial(),
            'about': getAbouts(),
            'link': getExternalLinks(),
        }

        return render(request, 'about.html', context)


class Trainers(ListView):

    def get(self, request, *args, **kwargs):
        try:
            trainer = Teacher.objects.filter(state=True)
        except:
            trainer = None

        context = {
            'trainer': trainer,
            'social': getSocial(),
            'about': getAbouts(),
            'link': getExternalLinks(),
        }
        return render(request, 'trainers.html', context)


class Lessons(ListView):

    def get(self, request, *args, **kwargs):
        try:
            lesson = Lesson.objects.filter(state=True)
        except:
            lesson = None

        context = {
            'lesson': lesson,
            'social': getSocial(),
            'about': getAbouts(),
            'link': getExternalLinks(),
        }
        return render(request, 'lessons.html', context)


class ContactView(View):
    form_class = ContactForm

    def get(self, request, *args, **kwargs):
        context = {
            'social': getSocial(),
            'about': getAbouts(),
            'link': getExternalLinks(),
            'form': self.form_class,
        }
        return render(request, 'contact.html', context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['email']
            body = render_to_string('email-templates.html', {'name': name, 'email': from_email, 'subject': subject, 'message': message})
            email = EmailMessage(subject, body, from_email, to=[settings.EMAIL_HOST_USER])
            email.content_subtype = 'html'
            email.send()
            return redirect('web:index')
        else:
            context = {
                'form': form
            }
            return render(request, 'contact.html', context)


class OffersView(ListView):

    def get(self, request, *args, **kwargs):
        try:
            offer = Offer.objects.filter(state=True, published=True).order_by('-create_to')
        except:
            offer: None

        context = {
            'offer': offer,
            'social': getSocial(),
            'about': getAbouts(),
            'link': getExternalLinks(),
        }
        return render(request, 'offer.html', context)


class DetailLessonForm(DetailView):
    def get(self, request, slug, *args, **kwargs):
        try:
            lesson = Lesson.objects.get(slug=slug)
        except:
            lesson = None

        context = {
            'lesson': lesson,
            'social': getSocial(),
            'about': getAbouts(),
            'link': getExternalLinks(),
        }
        return render(request, 'detail_lesson.html', context)


class TestRequestView(View):
    form_class = TestRequestForm

    def get(self, request, *args, **kwargs):
        context = {
            'social': getSocial(),
            'about': getAbouts(),
            'link': getExternalLinks(),
            'form': self.form_class,
        }

        return render(request, 'test-form.html', context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('web:index')
        else:
            context = {
                'form': form
            }
            return redirect(request, 'test-form.html', context)


