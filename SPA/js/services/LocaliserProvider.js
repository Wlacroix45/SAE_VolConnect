import { LOCALISER } from "../config.js";

export default class LocaliserProvider {
    static fetchLocalisations = async () => {
        try {
            const response = await fetch(`${LOCALISER}`);
            const json = await response.json();
            return json;
        } catch (err) {
            console.log('Error getting documents.', err);
            return [];
        }
    }

    static addLocalisation = async (id_aeroport, id_compagnie) => {
        const options = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                id_aeroport: Number(id_aeroport),
                id_compagnie: Number(id_compagnie),
            })
        };

        try {
            const response = await fetch(`${LOCALISER}`, options);
            const json = await response.json();
            return json;
        } catch (err) {
            console.log('Error creating document', err);
        }
    }

    static deleteLocalisation = async (id_aeroport, id_compagnie) => {
        const options = {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
            },
        };

        try {
            const response = await fetch(`${LOCALISER}/${id_aeroport}/${id_compagnie}`, options);
            return response.ok;
        } catch (err) {
            console.log('Error deleting document', err);
            return false;
        }
    }
}
