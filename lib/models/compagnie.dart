import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

class Compagnie {
  int id_compagnie ;
  String nom_comp;
  String uri;
  Compagnie({required this.id_compagnie,required this.nom_comp, required this.uri});
  static Compagnie fromJson(Map<String,dynamic >json) {
    final tags = <String>[];
    return Compagnie(
      id_compagnie: json['id_compagnie'],
      nom_comp: json['nom_comp'],
      uri: json['uri']
    );
  }
}