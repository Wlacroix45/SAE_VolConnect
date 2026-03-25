import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';


class Aeroport {
  int id_aeroport;
  String nom_aeroport;
  String ville ;
  String pays ;
  Aeroport({required this.id_aeroport,required this.nom_aeroport,required this.ville, required this.pays});

  static Aeroport fromJson(Map<String,dynamic >json) {
    final tags = <String>[];
    return Aeroport(
      id_aeroport: json['id_aeroport'],
      nom_aeroport: json['nom_aeroport'],
      ville: json['ville'],
      pays: json['pays'],
    );
  }
}