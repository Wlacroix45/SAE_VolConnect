import 'package:flutter/material.dart';
import 'package:volconnect/API/apiRest.dart';
import '../models/compagnie.dart';

class Compagniesview extends StatelessWidget{
  Compagniesview({super.key});

  @override
  Widget build(BuildContext context) {
    Future<List<Compagnie>> compagnie = APIRest().getCompagnies();

    return FutureBuilder <List<Compagnie>>(
        future: compagnie,
        builder: (BuildContext context, AsyncSnapshot<List<Compagnie>> snapshot) {
          if (snapshot.hasData) {
            return ListView.builder(
              itemBuilder : (BuildContext context ,int index) {
                return Card(
                  color: Colors.black,
                  elevation: 7,
                  margin: const EdgeInsets.all(10),
                  child:ListTile(
                    leading: CircleAvatar(backgroundColor: Colors.purple, child:Text(snapshot.data?[index].id_compagnie.toString()??""),),
                    title: Text(snapshot.data?[index].nom_comp??""),
                    trailing: IconButton(
                      icon: const Icon(Icons.edit),
                      onPressed: () {
                      },
                    ),
                  ),
                );
              },

            );
          }
          else if (snapshot.hasError) {
            return Center(child: Text('Error: ${snapshot.error}'));
          }
          else {
            return Center(child: CircularProgressIndicator());

          }
          return Container();
        }
    );


  }
}