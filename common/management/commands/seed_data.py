from django.core.management.base import BaseCommand
from faker import Faker
import random

from reports.models import Report
from skills.models import Skill, SkillCategory
from marketplace.models import MarketplaceItem, MarketplaceCategory
from common.models import Announcement


class Command(BaseCommand):
    help = "Seed database with realistic fake data"

    def handle(self, *args, **kwargs):

        fake = Faker()

        # Clear old data (optional but useful)
        Report.objects.all().delete()
        Skill.objects.all().delete()
        MarketplaceItem.objects.all().delete()
        Announcement.objects.all().delete()

        # -------------------------
        # Announcement
        # -------------------------
        Announcement.objects.create(
            title="Community Notice",
            content=fake.paragraph(nb_sentences=5),
            is_active=True
        )

        # -------------------------
        # Reports
        # -------------------------
        statuses = [
            Report.Status.OPEN,
            Report.Status.IN_PROGRESS,
            Report.Status.RESOLVED,
        ]

        for _ in range(8):
            Report.objects.create(
                title=fake.sentence(nb_words=6),
                description=fake.paragraph(nb_sentences=4),
                location=fake.city(),
                status=random.choice(statuses),
            )

        # -------------------------
        # Skill Categories
        # -------------------------
        skill_category_names = [
            "IT Support", "Plumbing", "Education",
            "Carpentry", "Gardening", "Electrical"
        ]

        skill_categories = []

        for name in skill_category_names:
            cat, _ = SkillCategory.objects.get_or_create(name=name)

            skill_categories.append(cat)

        # -------------------------
        # Skills
        # -------------------------
        levels = [
            Skill.Level.BEGINNER,
            Skill.Level.INTERMEDIATE,
            Skill.Level.ADVANCED,
        ]

        for _ in range(8):
            skill = Skill.objects.create(
                name=fake.job(),
                description=fake.paragraph(nb_sentences=3),
                level=random.choice(levels),
                contact_name=fake.name(),
                contact_phone="08" + "".join([str(random.randint(0,9)) for _ in range(8)]),

            )
            skill.categories.set(random.sample(skill_categories, 2))

        # -------------------------
        # Marketplace Categories
        # -------------------------
        mp_category_names = [
            "Electronics", "Furniture", "Sports",
            "Books", "Home Supplies"
        ]

        mp_categories = []

        for name in mp_category_names:
            cat, _ = MarketplaceCategory.objects.get_or_create(name=name)

            mp_categories.append(cat)

        # -------------------------
        # Marketplace Items
        # -------------------------
        types = [
            MarketplaceItem.Type.OFFER,
            MarketplaceItem.Type.WANTED,
            MarketplaceItem.Type.GIVEAWAY,
        ]
        conditions = [
            MarketplaceItem.Condition.NEW,
            MarketplaceItem.Condition.USED,
        ]

        for _ in range(8):
            MarketplaceItem.objects.create(
                title=fake.sentence(nb_words=5),
                description=fake.paragraph(nb_sentences=3),
                type=random.choice(types),
                condition=random.choice(conditions),
                contact_name=fake.name(),
                contact_phone="08" + "".join([str(random.randint(0,9)) for _ in range(8)]),

                category=random.choice(mp_categories),
            )

        self.stdout.write(self.style.SUCCESS("Database seeded with Faker data!"))
