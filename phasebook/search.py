from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    if args:
        filtered_users = []
        for user in USERS:

            if (    
                    args.get("id", "").lower() == user["id"].lower()  or 
                    args.get("name", "").lower() in user["name"].lower() and args.get("name","") != "" or
                    args.get("age", "") in [str(user["age"]-1), str(user["age"]), str(user["age"]+1)] or
                    args.get("occupation", "").lower() in user["occupation"].lower() and args.get("occupation","") != ""
                ):
                
                filtered_users.append(user)

        #FOR THE BONUS ROUND -- WITH SORTING BASED ON PRIORITY

        def sort(user):
            val = 0
            for key in [*args]:
                val = [*args].index(key)
                if str(args[key]).lower() in str(user[key]).lower():
                    val += 1 
                    return val  
            return val
            
        filtered_users.sort(key=sort)

        return filtered_users

    return USERS