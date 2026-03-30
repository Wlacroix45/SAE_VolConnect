import 'package:flutter/material.dart';
import '../models/vol.dart';

class VolDetailView extends StatelessWidget {
  final Vol vol;

  const VolDetailView({super.key, required this.vol});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(vol.nom_Vol),
        backgroundColor: Colors.green,
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
                  leading: const Icon(Icons.flight_takeoff, color: Colors.green),
                  title: const Text("Départ"),
                  subtitle: Text(vol.date_depart),
                ),
                ListTile(
                  leading: const Icon(Icons.flight_land, color: Colors.green),
                  title: const Text("Arrivée"),
                  subtitle: Text(vol.date_arrivee),
                ),
                const Divider(),
                ListTile(
                  leading: const Icon(Icons.business, color: Colors.green),
                  title: const Text("ID Compagnie"),
                  subtitle: Text(vol.id_compagnie.toString()),
                ),
                ListTile(
                  leading: const Icon(Icons.terminal, color: Colors.green),
                  title: const Text("Terminal Départ"),
                  subtitle: Text(vol.id_terminal_depart.toString()),
                ),
                ListTile(
                  leading: const Icon(Icons.terminal, color: Colors.green),
                  title: const Text("Terminal Arrivée"),
                  subtitle: Text(vol.id_terminal_arrive.toString()),
                ),
                const Divider(),
                ListTile(
                  leading: const Icon(Icons.info_outline, color: Colors.green),
                  title: const Text("ID Vol"),
                  subtitle: Text(vol.id_vol.toString()),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
