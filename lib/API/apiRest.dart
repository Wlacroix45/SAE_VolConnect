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
  Future<List<Compagnie>> getCompagnies() async{
    await Future.delayed(Duration(seconds: 1));
    final dataString = await http.get(Uri.parse('http://127.0.0.1:5000/compagnies'));
    final List<dynamic> json = jsonDecode(dataString.body);
    final todos = <Compagnie>[];
    for(var element in json){
      todos.add(Compagnie.fromJson(element));
    };
    return todos;
  }
  Future<List<Vol>> getVols() async{
    await Future.delayed(Duration(seconds: 1));
    final dataString = await http.get(Uri.parse('http://127.0.0.1:5000/vols'));
    final List<dynamic> json = jsonDecode(dataString.body);
    final todos = <Vol>[];
    for(var element in json){
      todos.add(Vol.fromJson(element));
    };
    return todos;
  }
  Future<List<Terminal>> getTerminaux() async{
    await Future.delayed(Duration(seconds: 1));
    final dataString = await http.get(Uri.parse('http://127.0.0.1:5000/terminaux'));
    final List<dynamic> json = jsonDecode(dataString.body);
    final todos = <Terminal>[];
    for(var element in json){
      todos.add(Terminal.fromJson(element));
    };
    return todos;
  }
  Future<List<Aeroport>> getAeroports() async{
    await Future.delayed(Duration(seconds: 1));
    final dataString = await http.get(Uri.parse('http://127.0.0.1:5000/aeroports'));
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