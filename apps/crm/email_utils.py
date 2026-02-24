from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings


def envoyer_email_bienvenue(prospect):
    """Email automatique à la création d'un prospect."""
    if not prospect.email:
        return False
    try:
        sujet  = f"Bonjour {prospect.nom_entreprise} — BizCRM"
        corps  = render_to_string('crm/emails/bienvenue.html', {'prospect': prospect})
        send_mail(
            subject      = sujet,
            message      = f"Bonjour {prospect.nom_entreprise}, merci de votre intérêt.",
            from_email   = settings.DEFAULT_FROM_EMAIL,
            recipient_list = [prospect.email],
            html_message = corps,
            fail_silently = False,
        )
        return True
    except Exception as e:
        print(f"Erreur email bienvenue : {e}")
        return False


def envoyer_email_relance(prospect, message_perso=''):
    """Email de relance manuel."""
    if not prospect.email:
        return False, "Ce prospect n'a pas d'adresse email."
    try:
        sujet = f"Relance commerciale — {prospect.nom_entreprise}"
        corps = render_to_string('crm/emails/relance.html', {
            'prospect':      prospect,
            'message_perso': message_perso,
        })
        send_mail(
            subject        = sujet,
            message        = message_perso or f"Bonjour {prospect.nom_entreprise}, nous revenons vers vous.",
            from_email     = settings.DEFAULT_FROM_EMAIL,
            recipient_list = [prospect.email],
            html_message   = corps,
            fail_silently  = False,
        )
        return True, "✅ Email envoyé avec succès !"
    except Exception as e:
        return False, f"❌ Erreur : {e}"
    @login_required
    def prospect_create(request):
     if request.method == 'POST':
        form = ProspectForm(request.POST)
        if form.is_valid():
            prospect = form.save(commit=False)
            prospect.cree_par = request.user
            prospect.save()
            # Email automatique de bienvenue
            if envoyer_email_bienvenue(prospect):
                messages.success(request, '✅ Prospect ajouté et email de bienvenue envoyé !')
            else:
                messages.success(request, '✅ Prospect ajouté avec succès !')
            return redirect('crm:prospect_list')
     else:
        form = ProspectForm()
    return render(request, 'crm/prospect_form.html', {'form': form, 'titre': 'Ajouter un prospect'})


    @login_required
    def envoyer_relance(request, pk):
     prospect = get_object_or_404(Prospect, pk=pk)

    if request.method == 'POST':
        message_perso = request.POST.get('message', '')
        success, msg  = envoyer_email_relance(prospect, message_perso)
        if success:
            messages.success(request, msg)
        else:
            messages.error(request, msg)
        return redirect('crm:prospect_detail', pk=pk)

    return render(request, 'crm/envoyer_relance.html', {'prospect': prospect})


def notifier_admin_nouveau_prospect(prospect):
    """Notifie l'admin quand un nouveau prospect est ajouté."""
    try:
        send_mail(
            subject    = f"🆕 Nouveau prospect : {prospect.nom_entreprise}",
            message    = f"Un nouveau prospect a été ajouté.\n\nEntreprise : {prospect.nom_entreprise}\nVille : {prospect.ville}\nSecteur : {prospect.get_secteur_display()}\nStatut : {prospect.get_statut_display()}",
            from_email = settings.DEFAULT_FROM_EMAIL,
            recipient_list = [settings.EMAIL_HOST_USER],  # ← ton propre email
            fail_silently  = True,
        )
    except Exception as e:
        print(f"Erreur notification admin : {e}")