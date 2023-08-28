from django.views.generic import TemplateView


class HomepageView(TemplateView):
    template_name = "base/home_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update(
            greeting_text="Welcome! If you want create contact or you mighty admin and want to generate"
            " contacts please click Contact Base.",
            #
            title="Home Page",
        )

        return context


class AboutUsView(TemplateView):
    template_name = "base/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update(
            about="Questions about this project you can send to telegram or email. "
            "Telegram: @ancient0007. "
            "Email: jenyaya0007@gmail.com.",
            title="About us",
        )

        return context
