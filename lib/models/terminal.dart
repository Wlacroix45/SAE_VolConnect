import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:volconnect/models/aeroport.dart';

class Terminal {
  int id_terminal;
  String nom_terminal;
  int id_aeroport ;
  String uri;
  Terminal({required this.id_terminal,required this.nom_terminal,required this.id_aeroport, required this.uri});
  //construit un Terminal depuis le json
  static Terminal fromJson(Map<String,dynamic >json) {
    final tags = <String>[];
    return Terminal(
      id_terminal: json['id_terminal'],
      nom_terminal: json['nom_terminal'],
      id_aeroport: json['id_aeroport'],
      uri: json['uri']
    );
  }

}