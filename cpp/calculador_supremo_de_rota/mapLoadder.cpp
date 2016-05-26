#include <mapLoadder.h>

#include <cstdint>
#include <iostream>

#include <osmium/io/any_input.hpp>
#include <osmium/handler.hpp>
#include <osmium/visitor.hpp>

void MapLoadder::node(osmium::Node&) {
    ++nodes;
}

void MapLoadder::way(osmium::Way&) {
    ++ways;
}

void MapLoadder::relation(osmium::Relation&) {
    ++relations;
}

MapLoadder::MapLoadder(){

}

MapLoadder::~MapLoadder(){

}
