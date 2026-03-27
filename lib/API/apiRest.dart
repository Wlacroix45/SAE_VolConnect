import 'dart:js_interop';

import 'package:flutter/material.dart';
import 'package:flutter/physics.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:flutter/services.dart';
import 'package:volconnect/models/aeroport.dart';
import 'package:volconnect/models/terminal.dart';
import '../models/compagnie.dart';
import '../models/vol.dart';
class APIRest{
  //récupère les données de l'API pour les compagnies
  Future<List<Compagnie>> getCompagnies() async{
    final dataString = await http.get(Uri.parse('http://localhost:5000/api/compagnies'));
    final List<dynamic> json = jsonDecode(dataString.body);
    final compagnies = <Compagnie>[];

    for(var element in json){
      compagnies.add(Compagnie.fromJson(element));
    };
    return compagnies;
  }
  //récupère les données de l'API pour les vols
  Future<List<Vol>> getVols() async{
    final dataString = await http.get(Uri.parse('http://localhost:5000/api/vols'));
    final List<dynamic> json = jsonDecode(dataString.body);
    final todos = <Vol>[];
    for(var element in json){
      todos.add(Vol.fromJson(element));
    };
    return todos;
  }
  //récupère les données de l'API pour les terminaux
  Future<List<Terminal>> getTerminaux() async{
    final dataString = await http.get(Uri.parse('http://127.0.0.1:5000/api/terminaux'));
    final List<dynamic> json = jsonDecode(dataString.body);
    final todos = <Terminal>[];
    for(var element in json){
      todos.add(Terminal.fromJson(element));
    };
    return todos;
  }
  //récupère les données de l'API pour les aeroports
  Future<List<Aeroport>> getAeroports() async{
    final dataString = await http.get(Uri.parse('http://127.0.0.1:5000/api/aeroports'));
    final List<dynamic> json = jsonDecode(dataString.body);
    final todos = <Aeroport>[];
    for(var element in json){
      todos.add(Aeroport.fromJson(element));
    };
    return todos;
  }

  Future<String> _loadAsset(String path) async {
    return rootBundle.loadString(path);
  }
}