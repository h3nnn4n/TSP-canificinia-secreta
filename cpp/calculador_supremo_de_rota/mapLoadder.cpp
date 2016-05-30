#include <mapLoadder.h>

#include <cstdint>
#include <iostream>

#include <string>

#include <osmium/io/any_input.hpp>
#include <osmium/handler.hpp>
#include <osmium/visitor.hpp>

void MapLoadder::load(std::string name) {
    osmium::io::File infile(name);
    osmium::io::Reader reader(infile);

    std::cout << "Loading map" << "\n";

    osmium::apply(reader, handler);

    std::cout << "Loaded:" << "\n";

    std::cout << "Nodes: "     << handler.nodes     << "\n";
    std::cout << "Ways: "      << handler.ways      << "\n";
    std::cout << "Relations: " << handler.relations << "\n";

    reader.close();
}

void MapLoadder::getInfo(){
    std::cout << "min lat: " << handler.lat_min << "\n";
    std::cout << "min lon: " << handler.lon_min << "\n";
    std::cout << "min lat: " << handler.lat_min << "\n";
    std::cout << "min lon: " << handler.lon_min << "\n";
}

MapLoadder::MapLoadder(){

}

MapLoadder::~MapLoadder(){

}
