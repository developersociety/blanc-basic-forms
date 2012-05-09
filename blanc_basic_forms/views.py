from django.views.generic import FormView, TemplateView
from django.core.urlresolvers import reverse_lazy
from django.conf import settings
from django.core import mail
from .forms import BasicForm


class BasicFormView(FormView):
    form_class = BasicForm
    template_name = 'forms/form.html'
    success_url = reverse_lazy('blanc_basic_forms:form-thanks')
    email_recipients = None
    email_subject = 'Contact Form'

    def form_valid(self, form):
        # Build up the email here, so any number of fields can be added
        form_data = []

        for i in form:
            form_data.append('%s: %s' % (i.label, i.data))

        body = '\n'.join(form_data)
        subject = u'%s%s' % (settings.EMAIL_SUBJECT_PREFIX, self.email_subject)

        # Default to managers if no recipients are specified
        recipients = self.email_recipients or [x[1] for x in settings.MANAGERS]

        # We open a connection and send multiple mails for recipient privacy
        connection = mail.get_connection()
        connection.open()

        for i in recipients:
            msg = mail.EmailMessage(subject, body, to=[i])
            connection.send_messages([msg])

        connection.close()

        return super(BasicFormView, self).form_valid(form)


class BasicFormThanksView(TemplateView):
    template_name = 'forms/thanks.html'
