#ifndef MAPLOADDER_H
#define MAPLOADDER_H

#include <cstdint>
#include <vector>

#include <osmium/io/any_input.hpp>
#include <osmium/handler.hpp>
#include <osmium/visitor.hpp>

struct CountHandler : public osmium::handler::Handler {
    uint64_t nodes = 0;
    uint64_t ways = 0;
    uint64_t relations = 0;

    std::vector<double> lat;
    std::vector<double> lon;

    double lon_min = 9999;
    double lon_max =-9999;
    double lat_min = 9999;
    double lat_max =-9999;

    void node(osmium::Node& node) {
        double la = node.location().lat();
        double lo = node.location().lon();

        lon_max = lon_max < lo ? lo : lon_max;
        lat_max = lat_max < la ? la : lat_max;
        lon_min = lon_min > lo ? lo : lon_min;
        lat_min = lat_min > la ? la : lat_min;

        lat.push_back(la);
        lon.push_back(lo);

        //std::cout << node.id() << "\t | " << ", " << node.location().lat() << "\n";
        ++nodes;
    }

    void way(osmium::Way&) {
        ++ways;
    }

    void relation(osmium::Relation&) {
        ++relations;
    }
};

class MapLoadder {
    private:
        CountHandler handler;

    public:
        MapLoadder();
        virtual ~MapLoadder();
        void load(std::string name);
        void getInfo();
};

#endif /* MAPLOADDER_H */
