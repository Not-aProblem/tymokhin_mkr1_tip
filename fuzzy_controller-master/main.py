import model
import inference_mamdani
import fuzzy_operators

# Quality_of_service (0-100), Quality_of_dishes(0-100)
inv = [30, 50]
inference_mamdani.preprocessing(model.input_lvs, model.output_lv)
result = inference_mamdani.process(model.input_lvs, model.output_lv, model.rule_base, inv)

print(inv)
print(result)

# for lv in model.input_lvs:
#     fuzzy_operators.draw_lv(lv)
# fuzzy_operators.draw_lv(model.output_lv)
