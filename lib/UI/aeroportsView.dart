import 'package:flutter/material.dart';
import 'package:volconnect/API/apiRest.dart';
import 'package:volconnect/models/aeroport.dart';
import 'aeroportDetailView.dart';

class Aeroportsview extends StatelessWidget {
  Aeroportsview({super.key});

  @override
  Widget build(BuildContext context) {
    Future<List<Aeroport>> todo = APIRest().getAeroports();

    return FutureBuilder<List<Aeroport>>(
        future: todo,
        builder: (BuildContext context, AsyncSnapshot<List<Aeroport>> snapshot) {
          if (snapshot.hasData) {
            return ListView.builder(
              itemCount: snapshot.data?.length ?? 0,
              itemBuilder: (BuildContext context, int index) {
                final aeroport = snapshot.data![index];
                return Card(
                  color: Colors.grey[200],
                  elevation: 4,
                  margin: const EdgeInsets.symmetric(horizontal: 10, vertical: 5),
                  child: ListTile(
                    leading: CircleAvatar(
                      backgroundColor: Colors.blue,
                      child: Text(aeroport.id_aeroport.toString()),
                    ),
                    title: Text(aeroport.nom_aeroport),
                    subtitle: Text("${aeroport.ville}, ${aeroport.pays}"),
                    trailing: const Icon(Icons.arrow_forward_ios, size: 16),
                    onTap: () {
                      Navigator.push(
                        context,
                        MaterialPageRoute(
                          builder: (context) => AeroportDetailView(aeroport: aeroport),
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
