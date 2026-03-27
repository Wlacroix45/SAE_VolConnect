import 'package:flutter/material.dart';
import 'package:volconnect/API/apiRest.dart';
import 'package:volconnect/models/aeroport.dart';

class Aeroportsview extends StatelessWidget{
  Aeroportsview({super.key});

  @override
  Widget build(BuildContext context) {
    Future<List<Aeroport>> todo = APIRest().getAeroports();

    return FutureBuilder <List<Aeroport>>(
        future: todo,
        builder: (BuildContext context, AsyncSnapshot<List<Aeroport>> snapshot) {
          if (snapshot.hasData) {
            return ListView.builder(
              itemBuilder : (BuildContext context ,int index) {
                return Card(
                  color: Colors.black,
                  elevation: 7,
                  margin: const EdgeInsets.all(10),
                  child:ListTile(
                    leading: CircleAvatar(backgroundColor: Colors.purple, child:Text(snapshot.data?[index].id_aeroport.toString()??""),),
                    title: Text(snapshot.data?[index].nom_aeroport??""),
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