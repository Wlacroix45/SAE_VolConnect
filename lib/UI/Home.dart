import 'package:flutter/material.dart';
import './aeroportsView.dart';
import './compagniesView.dart';
import './volsView.dart';

void main() => runApp(const BottomNavigationBarVolApp());

class BottomNavigationBarVolApp extends StatelessWidget {

  const BottomNavigationBarVolApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const BottomNavigationBarVol();
  }
}
class BottomNavigationBarVol extends StatefulWidget {
  const BottomNavigationBarVol({super.key});

  @override
  State<BottomNavigationBarVol> createState() => _BottomNavigationBarVolState();
}

class _BottomNavigationBarVolState extends State<BottomNavigationBarVol> {
  int _selectedIndex = 0;
  static const TextStyle optionStyle = TextStyle(fontSize: 30, fontWeight: FontWeight.bold);
  static List<Widget> _widgetOptions = <Widget>[
    Aeroportsview(),
    Compagniesview(),
    Volsview(),
  ];

  void _onItemTapped(int index) {
    setState(() {
      _selectedIndex = index;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('SAE vol connect', style: Theme.of(context).appBarTheme.titleTextStyle)),  // A modifier ici , style : Theme.of(context).appBarTheme.titleTextStyle
      body: Center(child: _widgetOptions.elementAt(_selectedIndex)),
      bottomNavigationBar: BottomNavigationBar(
        items: const <BottomNavigationBarItem>[
          BottomNavigationBarItem(icon: Icon(Icons.home), label: 'aeroports'),
          BottomNavigationBarItem(icon: Icon(Icons.business), label: 'compagnies'),
          BottomNavigationBarItem(icon: Icon(Icons.favorite_border), label: 'vols'),
        ],
        currentIndex: _selectedIndex,
        selectedItemColor: Colors.amber[800],
        onTap: _onItemTapped,
      ),
    );
  }
}