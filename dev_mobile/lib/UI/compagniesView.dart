import 'package:flutter/material.dart';
import 'package:volconnect/API/apiRest.dart';
import '../models/compagnie.dart';
import 'compagnieDetailView.dart';

class Compagniesview extends StatefulWidget {
  const Compagniesview({super.key});

  @override
  State<Compagniesview> createState() => _CompagniesviewState();
}

class _CompagniesviewState extends State<Compagniesview> {
  late Future<List<Compagnie>> _compagniesFuture;
  List<Compagnie> _allCompagnies = [];
  List<Compagnie> _filteredCompagnies = [];
  String _searchQuery = "";
  bool _isLoaded = false;

  @override
  void initState() {
    super.initState();
    _compagniesFuture = APIRest().getCompagnies();
  }

  void _filterCompagnies(String query) {
    setState(() {
      _searchQuery = query;
      _filteredCompagnies = _allCompagnies.where((compagnie) {
        final nom = compagnie.nom_comp.toLowerCase();
        final searchLower = query.toLowerCase();
        return nom.contains(searchLower);
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
              labelText: 'Rechercher une compagnie...',
              prefixIcon: const Icon(Icons.search),
              border: OutlineInputBorder(
                borderRadius: BorderRadius.circular(10),
              ),
              suffixIcon: _searchQuery.isNotEmpty
                  ? IconButton(
                      icon: const Icon(Icons.clear),
                      onPressed: () {
                        _filterCompagnies("");
                      },
                    )
                  : null,
            ),
            onChanged: _filterCompagnies,
          ),
        ),
        Expanded(
          child: FutureBuilder<List<Compagnie>>(
            future: _compagniesFuture,
            builder: (BuildContext context, AsyncSnapshot<List<Compagnie>> snapshot) {
              if (snapshot.connectionState == ConnectionState.waiting && !_isLoaded) {
                return const Center(child: CircularProgressIndicator());
              } else if (snapshot.hasError) {
                return Center(child: Text('Erreur: ${snapshot.error}'));
              } else if (snapshot.hasData) {
                if (!_isLoaded) {
                  _allCompagnies = snapshot.data!;
                  _filteredCompagnies = _allCompagnies;
                  _isLoaded = true;
                }

                if (_filteredCompagnies.isEmpty) {
                  return const Center(child: Text("Aucune compagnie trouvée"));
                }

                return ListView.builder(
                  itemCount: _filteredCompagnies.length,
                  itemBuilder: (BuildContext context, int index) {
                    final item = _filteredCompagnies[index];
                    return Card(
                      color: Colors.grey[200],
                      elevation: 4,
                      margin: const EdgeInsets.symmetric(horizontal: 10, vertical: 5),
                      child: ListTile(
                        leading: CircleAvatar(
                          backgroundColor: Colors.purple,
                          child: Text(item.id_compagnie.toString()),
                        ),
                        title: Text(item.nom_comp),
                        trailing: const Icon(Icons.arrow_forward_ios, size: 16),
                        onTap: () {
                          Navigator.push(
                            context,
                            MaterialPageRoute(
                              builder: (context) => CompagnieDetailView(compagnie: item),
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
