from .models import Employe
from django.shortcuts import render, redirect
from .models import Conge
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib import messages
from .form import CongeForm
from django.contrib.auth.decorators import user_passes_test



def home(request):
    """Page d'accueil simple pour présenter l'API"""
    return render(request, 'base.html')

def login_view(request):  # Correction de la faute de frappe dans le nom de la fonction
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = login(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('abonne')  # Redirigez vers la page d'accueil ou une autre page
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})  # Correction de l'indentation

    return render(request, 'login.html')  # Correction du nom du template
def logout_view(request):
    logout(request)
    messages.success(request, "Vous avez été déconnecté avec succès.")
    return redirect('authetification')
def liste_employes(request):
    employes = Employe.objects.all()
    return render(request, "employes/liste.html", {"employes": employes})

@login_required
def mes_conges(request):
    # Récupérer toutes les demandes de congé de l'utilisateur connecté
    conges = Conge.objects.filter(demandeur=request.user).order_by('-date_demande')
    
    # Tu peux préparer un dictionnaire pour la couleur du statut si tu veux
    statut_colors = {
        'approuve': 'success',   # vert
        'en_attente': 'warning', # orange
        'refuse': 'danger',      # rouge
        'plus_info': 'info',     # bleu ou jaune selon ton choix
    }

    return render(request, "conge.html", {
        "conges": conges,
        "statut_colors": statut_colors
    })


@login_required
def demander_conge(request):
    if request.method == "POST":
        form = CongeForm(request.POST)
        if form.is_valid():
            conge = form.save(commit=False)
            conge.demandeur = request.user  # on associe l'utilisateur connecté
            conge.save()
            messages.success(request, "Votre demande de congé a été soumise avec succès !")
            return redirect("mes_conges")
    else:
        form = CongeForm()

    return render(request, "demande.html", {"form": form})

@user_passes_test(lambda u: u.is_staff)  # accessible uniquement aux admin/staff
def admin_conges(request):
    # Récupération de tous les congés
    conges = Conge.objects.all().order_by('-date_demande')

    # Si une recherche est effectuée
    query = request.GET.get('q')
    if query:
        # Cherche les agents dont le username contient le texte
        conges = conges.filter(demandeur__username__icontains=query)

        # Calcul du nombre total de congés pour cet agent
        agent_conges_count = Conge.objects.filter(demandeur__username__icontains=query).count()
    else:
        agent_conges_count = None

    if request.method == "POST":
        conge_id = request.POST.get("conge_id")
        statut = request.POST.get("statut")
        conge = Conge.objects.get(id=conge_id)
        conge.statut = statut
        conge.save()
        messages.success(request, f"{conge.demandeur.username} - Statut mis à jour avec succès.")
        return redirect('/dash/')  # ou "admin_conges" si tu as mis le name

    return render(
        request,
        "admin.html",
        {
            "conges": conges,
            "agent_conges_count": agent_conges_count,
            "query": query,
        }
    )
@login_required
def redirect_after_login(request):
    if request.user.is_staff:  # si c'est un admin/staff
        return redirect('/dash/')  # vers ta page admin
    else:  # utilisateur normal
        return redirect('/conge/')  # vers la page employé
