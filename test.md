# 🏠 Système de Tarification Dynamique des Leads - Sakan

## 📋 Vue d'ensemble

Ce système calcule automatiquement le prix d'achat des leads immobiliers en fonction de plusieurs critères pour offrir une tarification juste et équitable.

**Prix de base : 50 crédits**  
**Fourchette finale : 35-150 crédits**

---

## 🧮 Formule de Calcul

```
Prix Final = Prix de Base × Multiplicateurs Principaux × Multiplicateurs Secondaires
```

### Multiplicateurs Principaux (Basés sur le formulaire)
1. **Mode d'acquisition**
2. **Type de bien**
3. **Nombre de chambres**
4. **Superficie**
5. **Budget**
6. **Délai souhaité**

### Multiplicateurs Secondaires (Contextuels)
1. **Fraîcheur du lead** (âge)
2. **Localisation** (ville)
3. **Urgence** (mots-clés)

---

## 📊 Détail des Multiplicateurs

### 1. Mode d'Acquisition
```javascript
// Les leads d'achat sont plus valorisés que la location
Acheter  → ×1.2 (+10 crédits)
Louer    → ×1.0 (prix de base)
```

### 2. Type de Bien
```javascript
// Biens commerciaux et de luxe = plus chers
Villa, Local commercial, Hangar, Local industriel → ×1.3 (+15 crédits)
Maison, Terrain                                  → ×1.1 (+5 crédits)
Appartement, Studio                              → ×1.0 (prix de base)
```

### 3. Nombre de Chambres
```javascript
// Plus de chambres = familles = leads plus précieux
5 chambres ou plus → ×1.2 (+10 crédits)
4 chambres         → ×1.1 (+5 crédits)
2-3 chambres       → ×1.0 (prix de base)
1 chambre          → ×0.9 (-5 crédits)
```

### 4. Superficie
```javascript
// Grandes surfaces = biens de valeur
200 m²+        → ×1.2 (+10 crédits)
150 - 200 m²   → ×1.1 (+5 crédits)
50 - 150 m²    → ×1.0 (prix de base)
< 50 m²        → ×0.9 (-5 crédits)
```

### 5. Budget
```javascript
// Budget élevé = client solvable = lead précieux
5M DH+              → ×1.4 (+20 crédits)
2M - 5M DH          → ×1.3 (+15 crédits)
1M - 2M DH          → ×1.2 (+10 crédits)
500 000 - 1M DH     → ×1.1 (+5 crédits)
< 500 000 DH        → ×1.0 (prix de base)
```

### 6. Délai Souhaité
```javascript
// Urgence = opportunité commerciale
Immédiatement      → ×1.3 (+15 crédits)
Dans le mois       → ×1.2 (+10 crédits)
Le mois prochain   → ×1.1 (+5 crédits)
Date fixe          → ×1.0 (prix de base)
```

### 7. Fraîcheur du Lead
```javascript
// Leads récents = plus de chances de conversion
< 6 heures   → ×1.15 (+7.5 crédits)
< 24 heures  → ×1.1 (+5 crédits)
< 72 heures  → ×1.0 (prix de base)
> 72 heures  → ×0.95 (-2.5 crédits)
```

### 8. Localisation
```javascript
// Villes premium = marché plus actif
Casablanca, Rabat, Marrakech     → ×1.15 (+7.5 crédits)
Fès, Tanger, Agadir, Meknès      → ×1.05 (+2.5 crédits)
Autres villes                    → ×1.0 (prix de base)
```

### 9. Urgence (Mots-clés)
```javascript
// Détection automatique de l'urgence dans la description
Mots "urgent", "rapidement", "vite", "immédiat" → ×1.05 (+2.5 crédits)
```

---

## 💡 Exemples Concrets

### Exemple 1: Lead Premium 💎
**Caractéristiques:**
- Mode: Acheter
- Type: Villa
- Chambres: 5 chambres ou plus
- Surface: 200 m²+
- Budget: 5M DH+
- Délai: Immédiatement
- Âge: 2 heures
- Ville: Casablanca
- Description: "Recherche urgent villa"

**Calcul:**
```
50 × 1.2 × 1.3 × 1.2 × 1.2 × 1.4 × 1.3 × 1.15 × 1.15 × 1.05 = 203 crédits
→ Plafonné à 150 crédits
```

### Exemple 2: Lead Standard 🏠
**Caractéristiques:**
- Mode: Louer
- Type: Appartement
- Chambres: 2 chambres
- Surface: 100-150 m²
- Budget: 500K-1M DH
- Délai: Le mois prochain
- Âge: 1 jour
- Ville: Fès
- Description: normale

**Calcul:**
```
50 × 1.0 × 1.0 × 1.0 × 1.0 × 1.1 × 1.1 × 1.1 × 1.05 × 1.0 = 70 crédits
```

### Exemple 3: Lead Budget 🏢
**Caractéristiques:**
- Mode: Louer
- Type: Studio
- Chambres: 1 chambre
- Surface: < 50 m²
- Budget: < 500K DH
- Délai: Date fixe
- Âge: 3 jours
- Ville: Petite ville
- Description: normale

**Calcul:**
```
50 × 1.0 × 1.0 × 0.9 × 0.9 × 1.0 × 1.0 × 1.0 × 1.0 × 1.0 = 40 crédits
```

---
## Final Price Range: 35-200 credits


## 📈 Avantages du Système

### ✅ Pour les Agents Immobiliers
- **Prix juste** : Payez selon la valeur réelle du lead
- **Leads frais** : Les nouveaux leads coûtent plus cher mais convertissent mieux
- **Ciblage précis** : Leads premium pour clients premium
- **Opportunités** : Leads urgents identifiés automatiquement

### ✅ Pour la Plateforme
- **Équité** : Tarification basée sur la valeur objective
- **Incitation qualité** : Encourage la soumission de leads détaillés
- **Optimisation** : Prix s'ajustent automatiquement à la demande
- **Transparence** : Critères de prix clairs et visibles

---

## 🔧 Implémentation Technique

### Fonction Principale
```javascript
const calculateLeadPrice = (lead) => {
  const basePrice = 50;
  
  // Multiplicateurs principaux (formulaire)
  const modeMultiplier = calculateModeMultiplier(lead.mode);
  const typeMultiplier = calculateTypeMultiplier(lead.type);
  const bedroomsMultiplier = calculateBedroomsMultiplier(lead.bedrooms);
  const surfaceMultiplier = calculateSurfaceMultiplier(lead.area);
  const budgetMultiplier = calculateBudgetMultiplier(lead.budget);
  const timingMultiplier = calculateTimingMultiplier(lead.timing);
  
  // Multiplicateurs secondaires (contextuels)
  const freshnessMultiplier = calculateFreshnessMultiplier(lead.created_at);
  const locationMultiplier = calculateLocationMultiplier(lead.address);
  const urgencyMultiplier = calculateUrgencyMultiplier(lead.timing, lead.description);
  
  const finalPrice = Math.round(
    basePrice * 
    modeMultiplier * typeMultiplier * bedroomsMultiplier * 
    surfaceMultiplier * budgetMultiplier * timingMultiplier *
    freshnessMultiplier * locationMultiplier * urgencyMultiplier
  );
  
  // Plafonnement entre 35-150 crédits
  return Math.max(35, Math.min(finalPrice, 150));
};
```

---

## 📊 Statistiques Attendues

| Type de Lead | Prix Moyen | Pourcentage |
|--------------|------------|-------------|
| Premium (Villa, Achat, Luxe) | 120-150 crédits | 10% |
| Standard (Appartement, Location) | 60-80 crédits | 70% |
| Budget (Studio, Petit budget) | 35-50 crédits | 20% |

---

## 🔄 Évolutions Futures

### Possibilités d'amélioration :
1. **Machine Learning** : Ajustement automatique basé sur les taux de conversion
2. **Saisonnalité** : Prix variables selon les périodes (été/hiver)
3. **Concurrence** : Ajustement selon l'offre/demande par zone
4. **Historique utilisateur** : Remises pour clients fidèles
5. **Qualité contact** : Bonus pour informations complètes

---

*Dernière mise à jour : Décembre 2024*
