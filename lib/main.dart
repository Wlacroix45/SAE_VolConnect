import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import './UI/Home.dart';
void main() {
  runApp(VolConnect());
}

class VolConnect extends StatelessWidget{
  @override
  Widget build(BuildContext context){
          return MaterialApp(
              title: 'TD2',
              home: BottomNavigationBarVolApp()
          );
  }
}