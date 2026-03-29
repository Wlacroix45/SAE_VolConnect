import VolProvider from "../../services/VolProvider.js";
import CompagnieProvider from "../../services/CompagnieProvider.js";

export default class Home{
    async render(){
        const MAX_UPCOMING = 7;

        const rawVols = await VolProvider.fetchVols(5000, 1, "");
        const vols = Array.isArray(rawVols)
            ? rawVols
            : (Array.isArray(rawVols.items) ? rawVols.items : []);

        const rawCompagnies = await CompagnieProvider.fetchCompagnies();
        const compagnies = Array.isArray(rawCompagnies)
          ? rawCompagnies
          : (Array.isArray(rawCompagnies.items) ? rawCompagnies.items : []);
        const compagnieById = new Map(
          compagnies
            .filter(c => c && c.id_compagnie != null)
            .map(c => [Number(c.id_compagnie), c])
        );

        const parseDate = (iso) => {
            if (!iso || typeof iso !== "string") return null;
            const d = new Date(iso);
            return Number.isNaN(d.getTime()) ? null : d;
        };

        const formatDateTime = (iso) => {
            const d = parseDate(iso);
            if (!d) return "";
            return d.toLocaleString("fr-FR", {
                year: "numeric",
                month: "2-digit",
                day: "2-digit",
                hour: "2-digit",
                minute: "2-digit",
            });
        };

        const now = new Date();
        const upcoming = vols
            .map(v => ({ vol: v, depart: parseDate(v?.date_heure_depart) }))
            .filter(x => x.depart && x.depart.getTime() >= now.getTime())
            .sort((a, b) => a.depart.getTime() - b.depart.getTime())
            .slice(0, MAX_UPCOMING);

        const upcomingCardsHtml = upcoming.length === 0
            ? `<p class="text-muted">Aucun vol à venir.</p>`
            : upcoming.map(({ vol }) => {
                const nomVol = vol?.nom_vol ?? "";
                const compagnieId = vol?.id_compagnie ?? "?";
                const terminalDepartId = vol?.id_terminal_depart ?? "?";
                const terminalArriveeId = vol?.id_terminal_arrivee ?? "?";
                const nomCompagnie = compagnieById.get(Number(compagnieId))?.nom_comp ?? `#${compagnieId}`;

                return `
                    <div class="card mb-3">
                      <div class="card-body">
                        <h5 class="card-title mb-1">${nomVol}</h5>
                        <div class="text-muted">Compagnie ${nomCompagnie}</div>
                        <div class="text-muted">Terminal #${terminalDepartId} ====> #${terminalArriveeId}</div>
                        <div class="mt-2">
                          <div><strong>Départ :</strong> ${formatDateTime(vol?.date_heure_depart)}</div>
                          <div><strong>Arrivée :</strong> ${formatDateTime(vol?.date_heure_arrivee)}</div>
                        </div>
                        <a class="btn btn-sm btn-outline-primary mt-3" href="#/vols/${vol?.id_vol}">Voir</a>
                      </div>
                    </div>
                `;
            }).join("");

        let view = `
            <div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
              <h1 class="h2">Dashboard</h1>
              <div class="btn-toolbar mb-2 mb-md-0"></div>
            </div>
        `;

        view += `
          <h2 class="h4">Prochains vols</h2>
          <div>
            ${upcomingCardsHtml}
          </div>
        `;
        return view;
    }
}



