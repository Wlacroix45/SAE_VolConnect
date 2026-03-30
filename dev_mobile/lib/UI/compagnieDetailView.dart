import 'package:flutter/material.dart';
import '../models/compagnie.dart';

class CompagnieDetailView extends StatelessWidget {
  final Compagnie compagnie;

  const CompagnieDetailView({super.key, required this.compagnie});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(compagnie.nom_comp),
        backgroundColor: Colors.purple,
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
                  leading: const Icon(Icons.business, color: Colors.purple),
                  title: const Text("Nom de la compagnie"),
                  subtitle: Text(compagnie.nom_comp),
                ),
                const Divider(),
                ListTile(
                  leading: const Icon(Icons.info_outline, color: Colors.purple),
                  title: const Text("ID Compagnie"),
                  subtitle: Text(compagnie.id_compagnie.toString()),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
