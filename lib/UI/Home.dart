import 'package:flutter/material.dart';
import './aeroportsView.dart';
import './compagniesView.dart';
import './volsView.dart';

void main() => runApp(const BottomNavigationBarExampleApp());

class BottomNavigationBarExampleApp extends StatelessWidget {

  const BottomNavigationBarExampleApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const BottomNavigationBarExample();
  }
}
class BottomNavigationBarExample extends StatefulWidget {
  const BottomNavigationBarExample({super.key});

  @override
  State<BottomNavigationBarExample> createState() => _BottomNavigationBarExampleState();
}

class _BottomNavigationBarExampleState extends State<BottomNavigationBarExample> {
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
      appBar: AppBar(title: Text('Flutter TD2', style: Theme.of(context).appBarTheme.titleTextStyle)),  // A modifier ici , style : Theme.of(context).appBarTheme.titleTextStyle
      body: Center(child: _widgetOptions.elementAt(_selectedIndex)),
      bottomNavigationBar: BottomNavigationBar(
        items: const <BottomNavigationBarItem>[
          BottomNavigationBarItem(icon: Icon(Icons.home), label: 'Home'),
          BottomNavigationBarItem(icon: Icon(Icons.business), label: 'Wabeille'),
          BottomNavigationBarItem(icon: Icon(Icons.favorite_border), label: 'Foucher'),
          BottomNavigationBarItem(icon: Icon(Icons.settings), label: 'Florence'),
        ],
        currentIndex: _selectedIndex,
        selectedItemColor: Colors.amber[800],
        onTap: _onItemTapped,
      ),
      floatingActionButton: _selectedIndex==0?FloatingActionButton(
        onPressed: (){
        },
        child: const Icon(Icons.add),
      ):const SizedBox.shrink(),
    );
  }
}