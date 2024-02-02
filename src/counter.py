from flask import Flask
import status

app = Flask(__name__)

COUNTERS = {}

# We will use the app decorator and create a route called slash counters.
# specify the variable in route <name>
# let Flask know that the only methods that is allowed to called
# on this function is "POST".

# GIVEN ------------------------------------------------------------------------
@app.route('/counters/<name>', methods=['POST'])
def create_counter(name):
    """Create a counter"""
    app.logger.info(f"Request to create counter: {name}")
    global COUNTERS
    if name in COUNTERS:
        return {"Message": f"Counter {name} already exists"}, status.HTTP_409_CONFLICT
    COUNTERS[name] = 0
    return {name: COUNTERS[name]}, status.HTTP_201_CREATED


# GIVEN ------------------------------------------------------------------------

# TASK ------------------------------------------------------------------------

# Step 1: Create a route for method PUT on endpoint /counters/<name>.
# Step 2: Create a function to implement that route.
@app.route('/counters/<name>', methods=['PUT'])
def update_counter(name):
    """Update a counter"""
    app.logger.info(f"Request to update counter: {name}")
    global COUNTERS
    if name in COUNTERS:
        # Step 3: Increment the counter by 1.
        COUNTERS[name] += 1
        # Step 4: Return the new counter and a 200_OK return code.
        return {name: COUNTERS[name]}, status.HTTP_200_OK

# TASK ------------------------------------------------------------------------

# > EXTRA ------------------------------------------------------------------------
@app.route('/counters/<name>', methods=['GET'])
def read_counter(name):
    """Read a counter"""
    app.logger.info(f"Request to read counter: {name}")
    return {name: COUNTERS[name]}, status.HTTP_200_OK







# > EXTRA ------------------------------------------------------------------------

