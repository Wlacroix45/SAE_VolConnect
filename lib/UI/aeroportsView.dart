import 'package:flutter/material.dart';
import 'package:volconnect/API/apiRest.dart';
import 'package:volconnect/models/aeroport.dart';
import 'aeroportDetailView.dart';

class Aeroportsview extends StatefulWidget {
  const Aeroportsview({super.key});

  @override
  State<Aeroportsview> createState() => _AeroportsviewState();
}

class _AeroportsviewState extends State<Aeroportsview> {
  late Future<List<Aeroport>> _aeroportsFuture;
  List<Aeroport> _allAeroports = [];
  List<Aeroport> _filteredAeroports = [];
  String _searchQuery = "";
  bool _isLoaded = false;

  @override
  void initState() {
    super.initState();
    _aeroportsFuture = APIRest().getAeroports();
  }

  void _filterAeroports(String query) {
    setState(() {
      _searchQuery = query;
      _filteredAeroports = _allAeroports.where((aeroport) {
        final nom = aeroport.nom_aeroport.toLowerCase();
        final ville = aeroport.ville.toLowerCase();
        final pays = aeroport.pays.toLowerCase();
        final searchLower = query.toLowerCase();
        return nom.contains(searchLower) || 
               ville.contains(searchLower) || 
               pays.contains(searchLower);
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
              labelText: 'Rechercher un aéroport, ville ou pays...',
              prefixIcon: const Icon(Icons.search),
              border: OutlineInputBorder(
                borderRadius: BorderRadius.circular(10),
              ),
              suffixIcon: _searchQuery.isNotEmpty
                  ? IconButton(
                      icon: const Icon(Icons.clear),
                      onPressed: () {
                        _filterAeroports("");
                      },
                    )
                  : null,
            ),
            onChanged: _filterAeroports,
          ),
        ),
        Expanded(
          child: FutureBuilder<List<Aeroport>>(
            future: _aeroportsFuture,
            builder: (BuildContext context, AsyncSnapshot<List<Aeroport>> snapshot) {
              if (snapshot.connectionState == ConnectionState.waiting && !_isLoaded) {
                return const Center(child: CircularProgressIndicator());
              } else if (snapshot.hasError) {
                return Center(child: Text('Erreur: ${snapshot.error}'));
              } else if (snapshot.hasData) {
                if (!_isLoaded) {
                  _allAeroports = snapshot.data!;
                  _filteredAeroports = _allAeroports;
                  _isLoaded = true;
                }

                if (_filteredAeroports.isEmpty) {
                  return const Center(child: Text("Aucun aéroport trouvé"));
                }

                return ListView.builder(
                  itemCount: _filteredAeroports.length,
                  itemBuilder: (BuildContext context, int index) {
                    final aeroport = _filteredAeroports[index];
                    return Card(
                      color: Colors.grey[200],
                      elevation: 4,
                      margin: const EdgeInsets.symmetric(horizontal: 10, vertical: 5),
                      child: ListTile(
                        leading: CircleAvatar(
                          backgroundColor: Colors.blue,
                          child: Text(aeroport.id_aeroport.toString()),
                        ),
                        title: Text(aeroport.nom_aeroport),
                        subtitle: Text("${aeroport.ville}, ${aeroport.pays}"),
                        trailing: const Icon(Icons.arrow_forward_ios, size: 16),
                        onTap: () {
                          Navigator.push(
                            context,
                            MaterialPageRoute(
                              builder: (context) => AeroportDetailView(aeroport: aeroport),
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
