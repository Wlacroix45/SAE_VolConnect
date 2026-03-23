import 'dart:js_interop';

import 'package:flutter/material.dart';
import 'package:flutter/physics.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:flutter/services.dart';
class MyAPIRest{
  Future<List<Compagnies>> getvols() async{
    await Future.delayed(Duration(seconds: 1));
    final dataString = await http.get(Uri.parse('http://127.0.0.1:5000/compagnies'));
    final List<dynamic> json = jsonDecode(dataString.body);
    final todos = <Todo>[];
    for(var element in json){
      todos.add(Todo.fromJson(element));
    };
    return todos;
  }
  Future<String> _loadAsset(String path) async {
    return rootBundle.loadString(path);
  }
}