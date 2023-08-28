from apps.contacts.models.contact import ContactDataType
from apps.contacts.services.faker_init import faker

# Possible data type and patterns
data_type_info = [
    (
        "Phone",
        r"^\+\d{12}$",
        "Phone number must be entered in the format: '+38XXXXXXXXXX'. Symbol + and 12 digits is allowed.",
    ),
    ("Email", r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$", "Email must contain @ and domain name"),
    ("Telegram", r"^[a-zA-Z0-9._%+-]$", "Telegram nickname"),
    ("LinkedIn", r"^[a-zA-Z0-9._%+-]$", "LinkedIn profile"),
]

data_type_instances = {}

for name, regex_pattern, message in data_type_info:
    data_type_instance, created = ContactDataType.objects.get_or_create(
        name=name, defaults={"regex_pattern": regex_pattern, "message": message}
    )
    data_type_instances[name] = data_type_instance


# Generator functions
def generate_phone_number():
    return f"+380{faker.unique.msisdn()[4:]}"


def generate_email():
    return faker.unique.email()


def generate_telegram():
    return f"@{faker.unique.user_name().lower()}"


def generate_linkedin():
    return f"linkedin.com/in/{faker.first_name()}-{faker.last_name()}-{faker.pystr_format(string_format='??######')}"


# Dictionary of generator functions
data_type_generators = {
    "Phone": generate_phone_number,
    "Email": generate_email,
    "Telegram": generate_telegram,
    "LinkedIn": generate_linkedin,
}

# List of data type instances
data_types = [data_type_instances[name] for name in data_type_generators.keys()]
