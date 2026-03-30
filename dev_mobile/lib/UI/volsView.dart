import 'package:flutter/material.dart';
import 'package:volconnect/API/apiRest.dart';
import '../models/vol.dart';
import 'volDetailView.dart';

class Volsview extends StatefulWidget {
  const Volsview({super.key});

  @override
  State<Volsview> createState() => _VolsviewState();
}

class _VolsviewState extends State<Volsview> {
  late Future<List<Vol>> _volsFuture;
  List<Vol> _allVols = [];
  List<Vol> _filteredVols = [];
  String _searchQuery = "";
  bool _isLoaded = false;

  @override
  void initState() {
    super.initState();
    _volsFuture = APIRest().getVols();
  }

  void _filterVols(String query) {
    setState(() {
      _searchQuery = query;
      _filteredVols = _allVols.where((vol) {
        final nomVol = vol.nom_Vol.toLowerCase();
        final searchLower = query.toLowerCase();
        return nomVol.contains(searchLower) || 
               vol.id_terminal_depart.toString().contains(query) ||
               vol.id_terminal_arrive.toString().contains(query);
      }).toList();
    });
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Padding(
          padding: const EdgeInsets.all(8.0),
          child: TextField(
            decoration: InputDecoration(
              labelText: 'Rechercher un vol ou terminal...',
              prefixIcon: const Icon(Icons.search),
              border: OutlineInputBorder(
                borderRadius: BorderRadius.circular(10),
              ),
              suffixIcon: _searchQuery.isNotEmpty
                  ? IconButton(
                      icon: const Icon(Icons.clear),
                      onPressed: () {
                        _filterVols("");
                      },
                    )
                  : null,
            ),
            onChanged: _filterVols,
          ),
        ),
        Expanded(
          child: FutureBuilder<List<Vol>>(
            future: _volsFuture,
            builder: (BuildContext context, AsyncSnapshot<List<Vol>> snapshot) {
              if (snapshot.connectionState == ConnectionState.waiting && !_isLoaded) {
                return const Center(child: CircularProgressIndicator());
              } else if (snapshot.hasError) {
                return Center(child: Text('Erreur: ${snapshot.error}'));
              } else if (snapshot.hasData) {
                if (!_isLoaded) {
                  _allVols = snapshot.data!;
                  _filteredVols = _allVols;
                  _isLoaded = true;
                }

                if (_filteredVols.isEmpty) {
                  return const Center(child: Text("Aucun vol trouvé"));
                }

                return ListView.builder(
                  itemCount: _filteredVols.length,
                  itemBuilder: (BuildContext context, int index) {
                    final vol = _filteredVols[index];
                    return Card(
                      color: Colors.grey[200],
                      elevation: 4,
                      margin: const EdgeInsets.symmetric(horizontal: 10, vertical: 5),
                      child: ListTile(
                        leading: CircleAvatar(
                          backgroundColor: Colors.green,
                          child: Text(vol.id_vol.toString()),
                        ),
                        title: Text(vol.nom_Vol),
                        subtitle: Text("Départ T${vol.id_terminal_depart} ➔ Arrivée T${vol.id_terminal_arrive}"),
                        trailing: const Icon(Icons.arrow_forward_ios, size: 16),
                        onTap: () {
                          Navigator.push(
                            context,
                            MaterialPageRoute(
                              builder: (context) => VolDetailView(vol: vol),
                            ),
                          );
                        },
                      ),
                    );
                  },
                );
              }
              return Container();
            },
          ),
        ),
      ],
    );
  }
}
