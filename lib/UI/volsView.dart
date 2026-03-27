import 'package:date_format/date_format.dart';
import 'package:flutter/material.dart';
import 'package:volconnect/API/apiRest.dart';
import '../models/vol.dart';

class Volsview extends StatelessWidget{
  Volsview({super.key});

  @override
  Widget build(BuildContext context) {
    Future<List<Vol>> vols = APIRest().getVols();

    return FutureBuilder <List<Vol>>(
        future: vols,
        builder: (BuildContext context, AsyncSnapshot<List<Vol>> snapshot) {
          if (snapshot.hasData) {
            return ListView.builder(
              itemBuilder : (BuildContext context ,int index) {
                return Card(
                  color: Colors.black,
                  elevation: 7,
                  margin: const EdgeInsets.all(10),
                  child:ListTile(
                    leading: CircleAvatar(backgroundColor: Colors.purple, child:Text(snapshot.data?[index].id_vol.toString()??""),),
                    title: Text(snapshot.data?[index].nom_Vol??""),
                    subtitle: Text(snapshot.data?[index].date_depart??""+"-"+snapshot.data![index].date_arrivee??""),
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