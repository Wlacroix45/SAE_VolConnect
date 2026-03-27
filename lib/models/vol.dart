import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
class Vol {
  int id_vol;
  int id_compagnie;
  int id_terminal_depart;
  int id_terminal_arrive;
  String date_depart;
  String date_arrivee;
  String nom_Vol;
  String uri;
  Vol({required this.id_vol,required this.id_compagnie,required this.id_terminal_depart,required
  this.id_terminal_arrive,required this.date_depart,required this.date_arrivee, required this.nom_Vol, required this.uri});

  static Vol fromJson(Map<String,dynamic >json) {
    final tags = <String>[];
    return Vol(
      id_vol: json['id_vol'],
      nom_Vol: json['nom_vol'],
      id_compagnie: json['id_compagnie'],
      id_terminal_depart: json['id_terminal_depart'],
      id_terminal_arrive: json['id_terminal_arrivee'],
      date_depart: json['date_heure_depart'],
      date_arrivee: json['date_heure_arrivee'],
      uri: json['uri'],
    );
  }
}