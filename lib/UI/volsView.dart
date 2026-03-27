import 'package:flutter/material.dart';
import 'package:volconnect/API/apiRest.dart';
import '../models/vol.dart';
import 'volDetailView.dart';

class Volsview extends StatelessWidget {
  Volsview({super.key});

  @override
  Widget build(BuildContext context) {
    Future<List<Vol>> vols = APIRest().getVols();

    return FutureBuilder<List<Vol>>(
        future: vols,
        builder: (BuildContext context, AsyncSnapshot<List<Vol>> snapshot) {
          if (snapshot.hasData) {
            return ListView.builder(
              itemCount: snapshot.data?.length ?? 0,
              itemBuilder: (BuildContext context, int index) {
                final vol = snapshot.data![index];
                return Card(
                  color: Colors.grey[200],
                  elevation: 4,
                  margin: const EdgeInsets.symmetric(horizontal: 10, vertical: 5),
                  child: ListTile(
                    leading: CircleAvatar(
                      backgroundColor: Colors.green,
                      child: Text(vol.id_vol.toString()),
                    ),
                    title: Text(vol.nom_Vol),
                    subtitle: Text("De ${vol.id_terminal_depart} à ${vol.id_terminal_arrive}"),
                    trailing: const Icon(Icons.arrow_forward_ios, size: 16),
                    onTap: () {
                      Navigator.push(
                        context,
                        MaterialPageRoute(
                          builder: (context) => VolDetailView(vol: vol),
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
