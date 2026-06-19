class Vehicle {
public:
    virtual string getType() = 0;
};

class Car : public Vehicle {
public:
    string getType() override {
        return "Car";
    }
};

class Bike : public Vehicle {
public:
    string getType() override {
        return "Bike";
    }
};

class Truck : public Vehicle {
public:
    string getType() override {
        return "Truck";
    }
};

class VehicleFactory {
public:
    virtual Vehicle* createVehicle() = 0;
};

class CarFactory : public VehicleFactory {
public:
    Car* createVehicle() override {
        return new Car{};
    }
};

class BikeFactory : public VehicleFactory {
public:
    Bike* createVehicle() override {
        return new Bike{};
    }
};

class TruckFactory : public VehicleFactory {
public:
    Truck* createVehicle() override {
        return new Truck{};
    }
};
