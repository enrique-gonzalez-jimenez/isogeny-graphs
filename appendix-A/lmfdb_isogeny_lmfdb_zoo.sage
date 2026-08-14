###############################################################################
# Appendix A: An LMFDB Zoo of Isogeny Graphs
#
# This script accompanies:
#
# Alexander J. Barrios, Enrique Gonzalez-Jimenez, and Ivan Novak,
# "Isogeny Graphs of Elliptic Curves in Characteristic Zero,"
# arXiv:2608.02494 (2026).
#
# Paper: https://arxiv.org/abs/2608.02494
# Repository: https://github.com/enrique-gonzalez-jimenez/isogeny-graphs
#
# The script searches the LMFDB for isogeny classes over Q and number fields
# with cm_type != 1. For each pair (class size, class degree), it selects a
# representative by prioritizing Q, then minimizing the field degree, absolute
# field discriminant, and conductor norm, in that order.
#
###############################################################################

from lmfdb import db


def validate_limit(name, value):
    """Validate that a scan limit is either None or a positive integer."""
    if value is None:
        return None

    value = ZZ(value)
    if value <= 0:
        raise ValueError("{} must be a positive integer or None".format(name))
    return value


def update_best(best, key, priority, label):
    """Keep the class with the smallest priority tuple for a given key."""
    if key not in best or priority < best[key][0]:
        best[key] = (priority, label)


def scan_rational_classes(best, max_classes=None):
    """Scan isogeny classes of elliptic curves defined over Q.

    The table ec_classdata already contains one record per rational isogeny
    class. Over Q, the field degree and absolute field discriminant are both 1,
    so rational classes are compared by conductor and then by LMFDB label.
    """
    rows = db.ec_classdata.search(
        {},
        projection=[
            "class_size",
            "class_deg",
            "conductor",
            "lmfdb_iso",
        ],
        limit=max_classes,
        sort=["conductor", "lmfdb_iso"],
    )

    scanned = 0

    for record in rows:
        scanned += 1

        key = (
            ZZ(record["class_size"]),
            ZZ(record["class_deg"]),
        )
        label = str(record["lmfdb_iso"])

        # The initial 0 gives every rational class priority over every class
        # defined over a number field of degree greater than 1.
        priority = (
            0,
            ZZ(record["conductor"]),
            label,
        )

        update_best(best, key, priority, label)

    return scanned


def scan_number_field_classes(best, max_classes=None):
    """Scan isogeny classes over number fields satisfying cm_type != 1.

    The condition number = 1 selects one curve from each isogeny class. The
    field degree and absolute field discriminant are read from the standard
    LMFDB field label d.r.D.i, where d is the degree and D is the absolute
    discriminant.
    """
    query = {
        "number": 1,
        "cm_type": {"$ne": 1},
    }

    rows = db.ec_nfcurves.search(
        query,
        projection=[
            "field_label",
            "conductor_norm",
            "class_size",
            "class_deg",
            "class_label",
            "label",
        ],
        limit=max_classes,
        sort=["field_label", "conductor_norm", "class_label"],
    )

    scanned = 0

    for record in rows:
        scanned += 1

        field_label_parts = record["field_label"].split(".")
        field_degree = ZZ(field_label_parts[0])
        absolute_field_discriminant = abs(ZZ(field_label_parts[2]))
        conductor_norm = ZZ(record["conductor_norm"])

        class_label = record.get("class_label")
        if class_label is None:
            class_label = record["label"].rsplit(".", 1)[0]
        class_label = str(class_label)

        key = (
            ZZ(record["class_size"]),
            ZZ(record["class_deg"]),
        )

        # The initial 1 places these classes after rational classes. Among
        # number fields, minimize degree, absolute discriminant, conductor
        # norm, and finally the label as a deterministic tie-breaker.
        priority = (
            1,
            field_degree,
            absolute_field_discriminant,
            conductor_norm,
            class_label,
        )

        update_best(best, key, priority, class_label)

    return scanned


def find_isogeny_pair_representatives(max_q_classes=None,
                                       max_nf_classes=None):
    """Find one preferred isogeny class for every (size, degree) pair.

    Selection order:

        1. Prefer a class defined over Q whenever one exists.
        2. Among rational classes, minimize the conductor.
        3. Otherwise, minimize the number-field degree.
        4. Then minimize the absolute field discriminant.
        5. Then minimize the conductor norm of the isogeny class.
        6. Use the LMFDB label only as a deterministic final tie-breaker.

    Set a limit to a positive integer for a test run. Set it to None to scan
    the complete corresponding database.
    """
    max_q_classes = validate_limit("max_q_classes", max_q_classes)
    max_nf_classes = validate_limit("max_nf_classes", max_nf_classes)

    best = {}

    q_scanned = scan_rational_classes(best, max_q_classes)
    nf_scanned = scan_number_field_classes(best, max_nf_classes)

    print("Scanned {} isogeny classes over Q.".format(q_scanned))
    print("Scanned {} isogeny classes over number fields.".format(nf_scanned))

    return best


def print_results(best):
    """Print rows ordered first by class size and then by class degree."""
    print("size, degree, LMFDB_label")

    for class_size, class_degree in sorted(best):
        label = best[(class_size, class_degree)][1]
        print("{}, {}, {}".format(class_size, class_degree, label))


# Test run: scan the first 1000 classes in each database.
# MAX_Q_CLASSES = 1000
# MAX_NF_CLASSES = 1000

# To scan both complete databases, use the following settings instead:
MAX_Q_CLASSES = None
MAX_NF_CLASSES = None

representatives = find_isogeny_pair_representatives(
    max_q_classes=MAX_Q_CLASSES,
    max_nf_classes=MAX_NF_CLASSES,
)
print_results(representatives)
