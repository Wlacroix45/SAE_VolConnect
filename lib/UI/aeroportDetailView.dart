import 'package:flutter/material.dart';
import 'package:volconnect/models/aeroport.dart';
class AeroportDetailView extends StatelessWidget {
  final Aeroport aeroport;

  const AeroportDetailView({super.key, required this.aeroport});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(aeroport.nom_aeroport),
        backgroundColor: Colors.blue,
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Card(
          elevation: 4,
          child: Padding(
            padding: const EdgeInsets.all(16.0),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              mainAxisSize: MainAxisSize.min,
              children: [
                ListTile(
                  leading: const Icon(Icons.location_city, color: Colors.blue),
                  title: const Text("Ville"),
                  subtitle: Text(aeroport.ville),
                ),
                const Divider(),
                ListTile(
                  leading: const Icon(Icons.public, color: Colors.blue),
                  title: const Text("Pays"),
                  subtitle: Text(aeroport.pays),
                ),
                const Divider(),
                ListTile(
                  leading: const Icon(Icons.info_outline, color: Colors.blue),
                  title: const Text("ID Aéroport"),
                  subtitle: Text(aeroport.id_aeroport.toString()),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
