import 'package:flutter/material.dart';
import 'package:volconnect/API/apiRest.dart';
import '../models/compagnie.dart';
import 'compagnieDetailView.dart';

class Compagniesview extends StatelessWidget {
  Compagniesview({super.key});

  @override
  Widget build(BuildContext context) {
    Future<List<Compagnie>> compagnie = APIRest().getCompagnies();

    return FutureBuilder<List<Compagnie>>(
        future: compagnie,
        builder: (BuildContext context, AsyncSnapshot<List<Compagnie>> snapshot) {
          if (snapshot.hasData) {
            return ListView.builder(
              itemCount: snapshot.data?.length ?? 0,
              itemBuilder: (BuildContext context, int index) {
                final item = snapshot.data![index];
                return Card(
                  color: Colors.grey[200],
                  elevation: 4,
                  margin: const EdgeInsets.symmetric(horizontal: 10, vertical: 5),
                  child: ListTile(
                    leading: CircleAvatar(
                      backgroundColor: Colors.purple,
                      child: Text(item.id_compagnie.toString()),
                    ),
                    title: Text(item.nom_comp),
                    trailing: const Icon(Icons.arrow_forward_ios, size: 16),
                    onTap: () {
                      Navigator.push(
                        context,
                        MaterialPageRoute(
                          builder: (context) => CompagnieDetailView(compagnie: item),
                        ),
                      );
                    },
                  ),
                );
              },
            );
          } else if (snapshot.hasError) {
            return Center(child: Text('Error: ${snapshot.error}'));
          } else {
            return const Center(child: CircularProgressIndicator());
          }
        });
  }
}
