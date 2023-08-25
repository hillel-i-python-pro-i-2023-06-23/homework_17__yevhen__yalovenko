from apps.contacts.models.contact import ContactDataType
from apps.contacts.services.faker_init import faker

phone_data_type = ContactDataType.objects.create(
    name="Phone",
    regex_pattern=r"^\?1?\d{9,15}$",
    message="Phone number must be entered in the format: '9999999999'. Up to 15 digits is allowed.",
)
email_data_type = ContactDataType.objects.create(
    name="Email",
    regex_pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$",
    message="Email must contain @ and domain name",
)
telegram_data_type = ContactDataType.objects.create(
    name="Telegram", regex_pattern=r"^[a-zA-Z0-9._%+-]$", message="Telegram nickname"
)
linked_in_type = ContactDataType.objects.create(
    name="LinkedIn", regex_pattern=r"^[a-zA-Z0-9._%+-]$", message="LinkedIn profile"
)


def generate_phone_number():
    return faker.unique.phone_number()


def generate_email():
    return faker.unique.email()


def generate_telegram():
    return f"@{faker.unique.user_name().lower()}"


def generate_linkedin():
    return f"linkedin.com/in/{faker.first_name()}-{faker.last_name()}-{faker.pystr_format(string_format='??######')}"


data_type_generators = {
    "Phone": generate_phone_number,
    "Email": generate_email,
    "Telegram": generate_telegram,
    "LinkedIn": generate_linkedin,
}

data_types = [phone_data_type, email_data_type, telegram_data_type, linked_in_type]
