from django.core.management.base import BaseCommand
from portfolio.models import GalleryItem, Experience, Skill


class Command(BaseCommand):
    help = 'Seed the portfolio with sample gallery items, experiences, and skills.'

    def handle(self, *args, **options):
        GalleryItem.objects.all().delete()
        Experience.objects.all().delete()
        Skill.objects.all().delete()

        gallery = [
            ('Echoes of the Hills', 'doc', 2025,
             'A documentary capturing the rhythms of mountain life in Mizoram.',
             'https://images.unsplash.com/photo-1596483941348-cb6d15e0fd60?w=1200&q=80'),
            ('Neon Pulse', 'music', 2025,
             'Experimental music video shot on a low-budget cinematic setup.',
             'https://images.unsplash.com/photo-1632187981988-40f3cbaeef5e?w=1200&q=80'),
            ('Court Dreams', 'film', 2024,
             'Short film about a small-town basketball team chasing the state title.',
             'https://images.pexels.com/photos/34612064/pexels-photo-34612064.jpeg?w=1200'),
            ('Studio Sessions', 'commercial', 2024,
             'Brand commercial cut from a 12-hour studio shoot.',
             'https://images.unsplash.com/photo-1574717024653-61fd2cf4d44d?w=1200&q=80'),
            ('Wild Frame', 'doc', 2024,
             'Wildlife short capturing the unseen colors of dawn.',
             'https://images.unsplash.com/photo-1625690303837-654c9666d2d0?w=1200&q=80'),
            ('Silhouettes', 'film', 2023,
             'A meditative piece on shadow and light.',
             'https://images.unsplash.com/photo-1576280314550-773c50583407?w=1200&q=80'),
            ('Crew Portraits', 'event', 2023,
             'Behind-the-scenes coverage of an indie film set.',
             'https://images.pexels.com/photos/3062542/pexels-photo-3062542.jpeg?w=1200'),
            ('Lens & Light', 'commercial', 2023,
             'Equipment-focused promotional cut.',
             'https://images.unsplash.com/photo-1602781975605-a032a4234333?w=1200&q=80'),
        ]
        for i, (title, cat, year, desc, img) in enumerate(gallery):
            GalleryItem.objects.create(
                title=title, category=cat, year=year,
                description=desc, image_url=img, order=i,
            )

        experiences = [
            ('Lead Videographer', 'Freelance', '2023 — Present',
             'Concept-to-delivery video production for indie artists, brands, and documentary projects.'),
            ('Video Editor', 'Hill Studios', '2022 — 2023',
             'Edited promotional and event content; established a fast-turnaround color pipeline.'),
            ('Production Assistant', 'Local Film Collective', '2021 — 2022',
             'On-set support, lighting, and second-camera operation across short film projects.'),
        ]
        for i, (role, company, period, desc) in enumerate(experiences):
            Experience.objects.create(
                role=role, company=company, period=period,
                description=desc, order=i,
            )

        skills = [
            ('Cinematography', 92), ('DaVinci Resolve', 88),
            ('Premiere Pro', 90), ('After Effects', 78),
            ('Color Grading', 85), ('Sound Design', 72),
            ('Storyboarding', 80), ('Drone Operation', 70),
        ]
        for i, (n, l) in enumerate(skills):
            Skill.objects.create(name=n, level=l, order=i)

        self.stdout.write(self.style.SUCCESS('✓ Portfolio seeded successfully.'))
