#ifndef MAPLOADDER_H
#define MAPLOADDER_H

#include <cstdint>

#include <osmium/io/any_input.hpp>
#include <osmium/handler.hpp>
#include <osmium/visitor.hpp>

class MapLoadder
{
    private:
        uint64_t nodes = 0;
        uint64_t ways = 0;
        uint64_t relations = 0;

    public:
        MapLoadder();
        virtual ~MapLoadder();
        void node(osmium::Node&) ;
        void way(osmium::Way&) ;
        void relation(osmium::Relation&) ;
};

#endif /* MAPLOADDER_H */
