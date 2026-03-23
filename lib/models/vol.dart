import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:intl/intl.dart';
class Vol {
  static int nb=0;
  int id_vol;
  int id_compagnie;
  int id_terminal_depart;
  int id_terminal_arrive;
  DateTime date_depart;
  DateTime date_arrivee;
  String nom_Vol;
  Task({required this.id,required this.title,required this.tags,required
  this.nbhours,required this.difficulty,required this.description});

  static List<Task> generateTask(int i){
    List<Task> tasks=[];
    for(int n=0;n<i;n++){
      tasks.add(Task(id: n, title: "title $n", tags: ['tag $n','tag${n+1}'], nbhours: n, difficulty: n, description: '$n'));
    }
    return tasks;
  }
  static Task fromJson(Map<String,dynamic >json){
    final tags=<String>[];
    if(json['tags']!=null){
      json['tags'].forEach((t){
        tags.add(t);
      }
      );

    }
    return Task(
        id: json['id'],
        title: json['title'],
        tags:tags,
        nbhours:json['nbhours'],
        difficulty: json['difficulty'],
        description: json['description']
    );
  }
  factory Task.newTask(){
    nb++; //attribut static de la classe.
    return Task(id: nb, title: 'title $nb', tags: ['tags $nb'], nbhours:
    nb, difficulty: nb%5, description: 'description $nb');
  }


}