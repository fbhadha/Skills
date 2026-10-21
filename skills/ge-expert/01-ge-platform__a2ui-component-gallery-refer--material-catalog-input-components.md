# Gemini Enterprise: platform, security, agents, cost, monitoring / A2UI component gallery reference: Material catalog input components to What's next to Import A2A agents from Agent Registry
Source: 01-Gemini-Enterprise-Platform-security-agents-cost-monitoring.pdf, pages 506-546, extracted 2026-10-18

Contains:
- A2UI component gallery reference: Material catalog input components to What's next (pages 506-536) https://docs.cloud.google.com/gemini/enterprise/docs/a2ui-agents/a2ui-component-gallery-reference
- Add and manage A2A agents from Google Cloud Marketplace (pages 537-540) https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-marketplace-agents
- Import A2A agents from Agent Registry (pages 541-546) https://docs.cloud.google.com/gemini/enterprise/docs/import-govern-agent-registry

## A2UI component gallery reference

URL: https://docs.cloud.google.com/gemini/enterprise/docs/a2ui-agents/a2ui-component-gallery-reference

### Material catalog input components

Input and form components allow users to enter text, make selections, and toggle options. 

#### MaterialButtonToggle

Material Design button toggle group for single selection. 

The following table outlines the properties available for the `MaterialButtonToggle` component: 

|Property|Requir|ed<sup>Default</sup><br>Value|Description|
|---|---|---|---|
|`value`|No|-|The currently selected value. This can be a literal string or a<br>reference to a value in the data model.|
|`options`|Yes|-|The list of options available for selection. Can be an array of<br>{label, value} objects or a data binding reference.|
|`disabled`|No|`false`|Whether the button toggle group is disabled.|
|`ariaLabel`|No|-|Discernible text for screen readers. Recommended for<br>accessibility when no visible label is present.|
|`aria`<br>`Labelledby`|No|-|Identifies the element (or elements) that labels the current<br>element. Used for accessibility.|
|`aria`<br>`Describedby`|No|-|Identifies the element (or elements) that describes the current<br>element. Used for accessibility.|
|`appearance`|No|`standard`|The appearance style of the button toggle group. One of:<br>"legacy", "standard".|
|`vertical`|No|`false`|Whether the button toggle group is arranged vertically.|
|`style`|No|-|Inline styles to apply to the element.|
|`weight`|No|-|Layout weight for the element when placed in a flex container.|

```
[
 {
   "id": "root",
   "component": "MaterialButtonToggle",
   "ariaLabel": "Text alignment",
   "value": {
     "path": "/user/alignment"
   },
   "options": [
     {
       "label": "Left",
       "value": "left"
     },
     {
       "label": "Center",
```

|Materia<br>Material<br>provide a<br>The follo<br>compone<br>`"`<br>`},`<br>`{`<br>`"`<br>`"`<br>`}`<br>`]`<br>`}`<br>`]`|lCheck<br>Design c<br>descrip<br>wing tab<br>nt:<br>`value":`<br>`label":`<br>`value":`|box<br>heckbox<br>tive labe<br>le outline<br>`"center"`<br>`"Right",`<br>`"right"`|component for boolean state. For optimal accessibility,<br>l or use ariaLabel for assistive technologies.<br>s the properties available for the<br>`MaterialCheckbox`<br> <br>|
|---|---|---|---|
|Property|Require|d<sup>Default</sup><br>Value|Description|
|`label`|No|-|The text label displayed next to the checkbox.|
|`checked`|No|`false`|Whether the checkbox is checked. This can be a literal boolean<br>or a reference to a value in the data model.|
|`disabled`|No|`false`|Whether the checkbox is disabled.|
|`color`|No|-|Color palette of the checkbox ("primary", "accent", "warn").|
|`label`<br>`Position`|No|`after`|Position of the label relative to the checkbox ("before", "after").|
|`ariaLabel`|No|-|Discernible text for screen readers. Recommended for<br>accessibility when no visible label is present.|
|`aria`<br>`Labelledb`<br>`y`|No|-|Identifies the element (or elements) that labels the current<br>element. Used for accessibility.|
|`aria`<br>`Described`<br>`by`|No|-|Identifies the element (or elements) that describes the current<br>element. Used for accessibility.|

|Property|Requir|ed<sup>Default</sup><br>Value|Description|
|---|---|---|---|
|`tooltip`|No|-|Tooltip text to display on hover.|
|`checks`|No|-|An array of validation rules (each containing a dynamic boolean<br>condition and an error message) that are reactively evaluated to<br>determine the input's validity.|
|`style`|No|-|Inline styles to apply to the element.|
|`weight`|No|-|Layout weight for the element when placed in a flex container.|

```
[
 {
   "id": "root",
   "component": "MaterialCheckbox",
   "label": "Agree to Terms and Conditions",
   "ariaLabel": "Agree to Terms and Conditions",
   "checked": {
     "path": "/user/agreedToTerms"
   },
   "color": "primary"
 }
]
```

#### MaterialChips

Material Design chip listbox component for single selection. The following table outlines the properties available for the `MaterialChips` component: 

|Property|Requi|red<sup>Default</sup><br>Value|Description|
|---|---|---|---|
|`value`|No|-|The currently selected value. This can be a literal string or a|
||||reference to a value in the data model.|

|Property|Requir|ed<sup>Default</sup><br>Value|Description|
|---|---|---|---|
|`options`|Yes|-|The list of chip options. Can be an array of {label, value}<br>objects or a data binding reference.|
|`disabled`|No|`false`|Whether the chip listbox is disabled.|
|`ariaLabel`|No|-|Discernible text for screen readers. Recommended for<br>accessibility when no visible label is present.|
|`aria`<br>`Labelledby`|No|-|Identifies the element (or elements) that labels the current<br>element. Used for accessibility.|
|`aria`<br>`Describedby`|No|-|Identifies the element (or elements) that describes the<br>current element. Used for accessibility.|
|`action`|No|-|The action to dispatch when a chip is selected.|
|`style`|No|-|Inline styles to apply to the element.|
|`weight`|No|-|Layout weight for the element when placed in a flex<br>container.|

```
[
 {
   "id": "root",
   "component": "MaterialChips",
   "ariaLabel": "Filter by status",
   "value": {
     "path": "/user/status"
   },
   "options": [
     {
       "label": "All",
       "value": "all"
     },
     {
       "label": "Active",
       "value": "active"
     },
     {
       "label": "Completed",
       "value": "completed"
     }
   ]
 }
]
```

#### MaterialDatepicker

Material Design datepicker component. 

The following table outlines the properties available for the `MaterialDatepicker` component: 

|Property|Require|d<sup>Default</sup><br>Value|Description|
|---|---|---|---|
|`label`|No|-|The label for the datepicker field.|
|`placehold`<br>`er`|No|-|The placeholder text.|
|`value`|No|-|The current selected date in ISO format.|
|`aria`<br>`Described`<br>`by`|No|-|Identifies the element (or elements) that describes the current<br>element. Used for accessibility.|
|`ariaLabel`|No|-|Discernible text for screen readers. Recommended for<br>accessibility when no visible label is present.|
|`aria`<br>`Labelledb`<br>`y`|No|-|Identifies the element (or elements) that labels the current<br>element. Used for accessibility.|
|`disabled`|No|`false`|Whether the datepicker is disabled.|
|`checks`|No|-|An array of validation rules (each containing a dynamic boolean<br>condition and an error message) that are reactively evaluated to<br>determine the input's validity.|
|`style`|No|-|Inline styles to apply to the element.|
|`weight`|No|-|Layout weight for the element when placed in a flex container.|

```
[
 {
   "id": "root",
   "component": "MaterialDatepicker",
   "label": "Appointment Date",
   "placeholder": "Choose a date",
   "ariaLabel": "Appointment Date",
   "value": {
     "path": "/appointment/date"
   }
 }
]
```

#### MaterialInput

Material Design text input field. 

The following table outlines the properties available for the `MaterialInput` component: 

|Property|Requi|red<sup>Default</sup><br>Value|Description|
|---|---|---|---|
|`label`|No|-|The label for the input field.|
|`placeholde`<br>`r`|No|-|The placeholder text.|
|`value`|No|-|The current value of the input. This can be a literal string or a<br>reference to a value in the data model.|
|`disabled`|No|`false`|Whether the input is disabled.|
|`name`|No|-|The name of the input element.|
|`readonly`|No|`false`|Whether the input is read-only.|
|`ariaLabel`|No|-|Discernible text for screen readers. Recommended for<br>accessibility when no visible label is present.|
|`aria`<br>`Labelledby`|No|-|Identifies the element (or elements) that labels the current<br>element. Used for accessibility.|

|Property|Requi|red<sup>Default</sup><br>Value|Description|
|---|---|---|---|
|`aria`<br>`Described`<br>`y`|`b`<br>No|-|Identifies the element (or elements) that describes the current<br>element. Used for accessibility.|
|`type`|No|`text`|The type of input control to display. One of: "text", "number",<br>"email", "tel", "date". "password" is not allowed.|
|`validatio`<br>`Regexp`|`n`<br>No|-|Regular expression for input validation.|
|`checks`|No|-|An array of validation rules (each containing a dynamic boolean<br>condition and an error message) that are reactively evaluated to<br>determine the input's validity.|
|`style`|No|-|Inline styles to apply to the element.|
|`weight`|No|-|Layout weight for the element when placed in a flex container.|

```
[
 {
   "id": "root",
   "component": "MaterialInput",
   "label": "First Name",
   "placeholder": "John",
   "value": {
     "path": "/user/firstName"
   }
 }
]
```

#### MaterialRadioButton

A2UI wrapper for the Angular Material Radio Button component. Supports single selection from a list of options within a radio group. 

The following table outlines the properties available for the `MaterialRadioButton` component: 

|Property|Requir|ed<sup>Default</sup><br>Value|Description|
|---|---|---|---|
|`value`|No|-|The currently selected value. Can be a literal string or a data<br>binding reference.|
|`options`|Yes|-|The list of radio options available. Can be an array of {label,<br>value} objects or a data binding reference.|
|`disabled`|No|`false`|Whether the radio group is disabled.|
|`ariaLabel`|No|-|Discernible text for screen readers. Recommended for<br>accessibility when no visible label is present.|
|`aria`<br>`Labelledby`|No|-|Identifies the element (or elements) that labels the current<br>element. Used for accessibility.|
|`aria`<br>`Describedb`|`y`<br>No|-|Identifies the element (or elements) that describes the current<br>element. Used for accessibility.|
|`color`|No|-|Color palette of the radio button ("primary", "accent", "warn").|
|`label`<br>`Position`|No|`after`|Position of the label relative to the radio button. One of:<br>"before", "after".|
|`style`|No|-|Inline styles to apply to the element.|
|`weight`|No|-|Layout weight for the element when placed in a flex container.|

```
[
 {
   "id": "root",
   "component": "MaterialRadioButton",
   "ariaLabel": "Delivery options",
   "value": {
     "path": "/order/deliverySpeed"
   },
   "options": [
     {
       "label": "Standard",
       "value": "standard"
     },
     {
       "label": "Express",
       "value": "express"
     },
     {
       "label": "Next Day",
       "value": "nextDay"
     }
   ],
   "color": "primary",
   "labelPosition": "after"
 }
]
```

#### MaterialSelect

Material Design select (drop-down) component for single selection. For optimal accessibility, always provide a descriptive label or use aria-label for assistive technologies. 

The following table outlines the properties available for the `MaterialSelect` component: 

|Property|Require|d<sup>Default</sup><br>Value|Description|
|---|---|---|---|
|`label`|No|-|The label for the select field.|
|`placehold`<br>`er`|No|-|The placeholder text shown when no value is selected.|
|`value`|No|-|The current selected value. This can be a literal string or a<br>reference to a value in the data model.|
|`options`|Yes|-|The list of options available for selection. Can be an array of<br>{label, value} objects or a data binding reference.|
|`disabled`|No|`false`|Whether the select component is disabled.|
|`ariaLabel`|No|-|Discernible text for screen readers. Recommended for<br>accessibility when no visible label is present.|
|`aria`<br>`Labelledb`<br>`y`|No|-|Identifies the element (or elements) that labels the current<br>element. Used for accessibility.|

|Property|Requir|ed<sup>Default</sup><br>Value|Description|
|---|---|---|---|
|`aria`<br>`Described`|No|-|Identifies the element (or elements) that describes the current<br>element. Used for accessibility.|
|`by`||||
|`checks`|No|-|An array of validation rules (each containing a dynamic boolean<br>condition and an error message) that are reactively evaluated to<br>determine the input's validity.|
|`style`|No|-|Inline styles to apply to the element.|
|`weight`|No|-|Layout weight for the element when placed in a flex container.|

```
[
 {
   "id": "root",
   "component": "MaterialSelect",
   "label": "Favorite Color",
   "placeholder": "Choose a color",
   "ariaLabel": "Select your favorite color",
   "value": {
     "path": "/user/favoriteColor"
   },
   "options": [
     {
       "label": "Red",
       "value": "red"
     },
     {
       "label": "Green",
       "value": "green"
     },
     {
       "label": "Blue",
       "value": "blue"
     }
   ]
 }
]
```

#### MaterialSlideToggle

A2UI wrapper for the Angular Material Slide Toggle component. Supports boolean toggle bindings and custom accessibility attributes. 

The following table outlines the properties available for the `MaterialSlideToggle` component: 

|Property|Require|d<sup>Default</sup><br>Value|Description|
|---|---|---|---|
|`label`|No|-|The text label displayed next to the slide toggle.|
|`checked`|No|`false`|Whether the slide toggle is checked. Can be a literal boolean<br>or a data binding reference.|
|`disabled`|No|`false`|Whether the slide toggle is disabled.|
|`required`|No|`false`|Whether the slide toggle is required.|
|`color`|No|-|Color palette of the toggle ("primary", "accent", "warn").|
|`label`<br>`Position`|No|`after`|Position of the label relative to the toggle ("before", "after").|
|`ariaLabel`|No|-|Discernible text for screen readers. Recommended for<br>accessibility when no visible label is present.|
|`aria`<br>`Labelledby`|No|-|Identifies the element (or elements) that labels the current<br>element. Used for accessibility.|
|`aria`<br>`Describedby`|No|-|Identifies the element (or elements) that describes the<br>current element. Used for accessibility.|
|`tooltip`|No|-|Tooltip text to display on hover.|
|`style`|No|-|Inline styles to apply to the element.|
|`weight`|No|-|Layout weight for the element when placed in a flex<br>container.|

```
[
 {
   "id": "root",
   "component": "MaterialSlideToggle",
   "label": "Enable notifications",
   "ariaLabel": "Enable notifications toggle",
   "checked": {
     "path": "/settings/notifications"
   },
   "color": "accent",
   "labelPosition": "after"
 }
]
```

#### MaterialSlider

A2UI wrapper for the Angular Material Slider component. Supports numeric value selection and range constraints. 

The following table outlines the properties available for the `MaterialSlider` component: 

|Property|Requi|red<sup>Default</sup><br>Value|Description|
|---|---|---|---|
|`value`|No|`0`|The current value of the slider. Can be a literal number or a<br>data binding reference.|
|`min`|No|`0`|The minimum value of the slider.|
|`max`|No|`100`|The maximum value of the slider.|
|`step`|No|`1`|The step increment of the slider.|
|`disabled`|No|`false`|Whether the slider is disabled.|
|`color`|No|-|Color palette of the slider ("primary", "accent", "warn").|
|`ariaLabel`|No|-|Discernible text for screen readers. Recommended for<br>accessibility when no visible label is present.|
|`aria`<br>`Labelledby`|No|-|Identifies the element (or elements) that labels the current<br>element. Used for accessibility.|
|`aria`<br>`Describedby`|No|-|Identifies the element (or elements) that describes the<br>current element. Used for accessibility.|

|Property|Requir|ed<sup>Default</sup><br>Value|Description|
|---|---|---|---|
|`style`|No|-|Inline styles to apply to the element.|
|`weight`|No|-|Layout weight for the element when placed in a flex<br>container.|

```
[
 {
   "id": "root",
   "component": "MaterialSlider",
   "min": 0,
   "max": 100,
   "step": 5,
   "value": {
     "path": "/audio/volume"
   },
   "color": "primary",
   "ariaLabel": "Volume adjustment"
 }
]
```

#### MaterialTimepicker

A2UI wrapper for the Angular Material Timepicker component. Supports time selection and form field integration. The following table outlines the properties available for the `MaterialTimepicker` component: 

|Property|Requi|red<sup>Default</sup><br>Value|Description|
|---|---|---|---|
|`label`|No|-|The text label for the timepicker field.|
|`placehold`<br>`er`|No|-|The placeholder text.|

|Property|Require|d<sup>Default</sup><br>Value|Description|
|---|---|---|---|
|`value`|No|-|The current selected time in ISO format. Can be a literal string or<br>a data binding reference.|
|`ariaLabel`|No|-|Discernible text for screen readers. Recommended for<br>accessibility when no visible label is present.|
|`aria`<br>`Labelledb`<br>`y`|No|-|Identifies the element (or elements) that labels the current<br>element. Used for accessibility.|
|`aria`<br>`Described`<br>`by`|No|-|Identifies the element (or elements) that describes the current<br>element. Used for accessibility.|
|`disabled`|No|`false`|Whether the timepicker is disabled.|
|`checks`|No|-|An array of validation rules (each containing a dynamic boolean<br>condition and an error message) that are reactively evaluated to<br>determine the input's validity.|
|`style`|No|-|Inline styles to apply to the element.|
|`weight`|No|-|Layout weight for the element when placed in a flex container.|
|`[`<br>`{`<br>`"id":`<br>`"comp`<br>`"labe`<br>`"plac`<br>`"aria`<br>`"valu`<br>`"pa`<br>`}`<br>`}`<br>`]`|`"root",`<br>`onent":`<br>`l": "Set`<br>`eholder"`<br>`Label":`<br>`e": {`<br>`th": "/a`|<br>`"Materi`<br>`Alarm"`<br>`: "Sele`<br>`"Set Al`<br>`larm/ti`|`alTimepicker",`<br>`,`<br>`ct time",`<br>`arm Time",`<br>`me"`|

### Basic catalog components

This section provides a reference for available A2UI basic catalog components. 

**Note:** Gemini Enterprise supports A2UI versions v0.9 and v0.8. For more information about A2UI versions, see Specification Versions (https://a2ui.org/#specification-versions) in the A2UI documentation. 

**Note:** The basic catalog is referred to as the "standard catalog" in v0.8. See the 0.8 component model documentation 

(https://a2ui.org/specification/v0.8-a2ui/#section-2-the-component-model) for information. 

### Basic catalog schema files

For more information on these properties, see: 

- **v0.9** basic catalog definition (JSON schema) 

(https://github.com/a2ui- 

project/a2ui/blob/main/specification/v0_9/catalogs/basic/catalog.json) 

- **v0.8** standard catalog definition (JSON schema) (https://a2ui.org/specification/v0_8/standard_catalog_definition.json) 

### Basic catalog common properties

All components, regardless of their specific type, share a set of common properties that can be configured: 

|Property|Requir|edDescription|
|---|---|---|
|`id`|Yes|A unique identifier for the component within the current surface.|
|`accessib`<br>`ity`|`il`<br>No|Attributes to improve accessibility, such as labels and roles.|
|`weight`|No|A value used in`Row`or`Column`layouts to control how much space the<br>component takes up relative to its siblings, similar to`flex-grow`.|

### Basic catalog layout components

Layout components are used to structure and arrange other components within the user interface. The following layout components are available: 

#### Row

A `Row` is a layout component used to arrange its child components horizontally, from left to right. It acts as a container where you can place multiple components side-by-side. The exact spacing and positioning of the children within the row can be controlled using the `justify` / `distribution` and `align` / `alignment` properties. 

The following table outlines the properties available for the `Row` component: 

|Property|Type/Values|Description|
|---|---|---|
|`children`|v0.9: Array of component IDs or<br>template definition<br>v0.8:`explicitList`or`template`|The child components to be arranged<br>horizontally within the Row.|
|`justify`<br>(v0.9)<br>`distribution`<br>(v0.8)|`start`,`center`,`end`,`spaceBetween`,<br>`spaceAround`,`spaceEvenly`|Controls how child components are<br>distributed along the horizontal axis.|
|`align`(v0.9)<br>`alignment`<br>(v0.8)|`start`,`center`,`end`,`stretch`|Controls how child components are<br>aligned on the vertical axis.|

v0.9 JSONv0.8 JSON (#v0.8-json) (#v0.9-json) 

```
{
```

- `"id": "toolbar",` 

- `"component": "Row",` 

- `"children": ["btn1", "btn2", "btn3"],` 

- `"justify": "spaceBetween",` 

- `"align": "center"` 

- `}` 

#### Column

A `Column` is a layout component used to arrange its child components vertically, from top to bottom. It acts as a container where you can place multiple components one below the other. The exact spacing and positioning of the children within the column can be controlled using the `justify` / `distribution` and `align` / `alignment` properties. 

The following table outlines the properties available for the `Column` component: 

|Property|Type/Values|Description|
|---|---|---|
|`children`|v0.9: Array of component IDs or<br>template definition<br>v0.8:`explicitList`or`template`|The child components to be arranged<br>vertically within the Column.|
|`justify`<br>(v0.9)<br>`distribution`<br>(v0.8)|`start`,`center`,`end`,`spaceBetween`,<br>`spaceAround`,`spaceEvenly`|Controls how child components are<br>distributed along the vertical axis.|
|`align`(v0.9)<br>`alignment`<br>(v0.8)|`start`,`center`,`end`,`stretch`|Controls how child components are<br>aligned on the horizontal axis.|

v0.9 JSONv0.8 JSON (#v0.8-json) (#v0.9-json) 

```
{
 "id": "content",
 "component": "Column",
 "children": ["header", "body", "footer"],
 "justify": "start",
 "align": "stretch"
}
```

#### List

A `List` is a layout component that displays a scrollable list of items. It supports static children and dynamic templates for generating items from data. The scroll direction can be vertical or horizontal. 

The following table outlines the properties available for the `List` component: 

|Property|Type/Values|Description|
|---|---|---|
|`children`|v0.9: Array of component IDs or<br>template definition<br>v0.8:`explicitList`or`template`|The items to be displayed in the list.|
|`direction`|`vertical`,`horizontal`|The scroll direction of the list.|
|`align`(v0.9)<br>`alignment`<br>(v0.8)|`start`,`center`,`end`,`stretch`|Controls how list items are aligned on<br>the cross axis.|

v0.9 JSONv0.8 JSON (#v0.8-json) (#v0.9-json) `{ "id": "message-list", "component": "List", "children": { "componentId": "message-item", "path": "/messages" }, "direction": "vertical" }` 

### Basic catalog display components

Display components are used to present information to the user. The following display components are available: 

#### Text

The `Text` component displays text content and supports various styling hints, such as headings, captions, and body text. 

The following table outlines the properties available for the `Text` component: 

|Property|Type/Values|Description|
|---|---|---|
|`text`|v0.9: String or`DataBinding`<br>v0.8:`BoundValue`|The text content to display.|
|`variant`(v0.9)<br>`usageHint`(v0.8)|`h1`,`h2`,`h3`,`h4`,`h5`,`caption`,`body`|Styling hint for the text.|

v0.9 JSONv0.8 JSON (#v0.8-json) (#v0.9-json) 

```
{
 "id": "title",
 "component": "Text",
 "text": "Welcome to A2UI",
 "variant": "h1"
}
```

#### Image

An `Image` component displays images from a specified URL and provides options to control how the image fits its container. 

The following table outlines the properties available for the `Image` component: 

|Property|Type/Values|Description|
|---|---|---|
|`url`|v0.9: String or`Data`<br>`Binding`<br>v0.8:`BoundValue`|The URL of the image to display.|
|`fit`|String|How the image should fit its container (e.g.,<br>"cover").|

Property Type/Values Description `variant` (v0.9) String Hint for usage or styling variants (e.g., "hero"). `usageHint` (v0.8) 

v0.9 JSONv0.8 JSON (#v0.8-json) (#v0.9-json) 

```
{
 "id": "hero",
 "component": "Image",
 "url": "https://example.com/hero.png",
 "fit": "cover",
 "variant": "hero"
}
```

#### Icon

The `Icon` component displays icons from a standard set defined in the catalog. 

The following table outlines the properties available for the `Icon` component: 

Property Type/Values Description `name` v0.9: String or `DataBinding` The name of the icon to display (e.g., "check"). v0.8: `BoundValue` 

v0.9 JSONv0.8 JSON (#v0.8-json) (#v0.9-json) 

```
{
 "id": "check-icon",
 "component": "Icon",
 "name": "check"
}
```

#### Divider

The `Divider` component displays a visual separator line, which can be either horizontal or vertical. 

The following table outlines the properties available for the `Divider` component: 

<!-- Start of picture text -->
Property Type/Values Description<br>axis horizontal ,  vertical The orientation of the divider line.<br>v0.9 JSONv0.8 JSON (#v0.8-json)<br>(#v0.9-json)<br>{<br> "id": "separator",<br> "component": "Divider",<br> "axis": "horizontal"<br>}<br><!-- End of picture text -->

### Basic catalog interactive components

Interactive components let you interact with the application, such as providing input or triggering actions. The following interactive components are available: 

#### Button

The `Button` component is a clickable element that triggers a specific action or event within the application. 

The following table outlines the properties available for the `Button` component: 

|Property|Type/Values|Description|
|---|---|---|
|`child`|Component ID|The ID of the component to display inside the button|
|||(e.g., a Text component).|

|Property|Type/Values|Description|
|---|---|---|
|`variant`|v0.9: String (e.g.,|The styling type or emphasis applied to the button.|
|(v0.9)|`"primary"`)||
|`primary`<br>(v0.8)|v0.8: Boolean||
|`action`|v0.9: Event Object (e.g.<br>keying `event`)<br>v0.8: Action Object (e.g.<br>keying `name`)|The action to trigger when the button is clicked.|

v0.9 JSONv0.8 JSON (#v0.8-json) (#v0.9-json) `{ "id": "submit-btn", "component": "Button", "child": "submit-text", "variant": "primary", "action": { "event": { "name": "submit_form" } } }` 

#### TextField

The `TextField` is an interactive component that lets you input text. It also supports optional validation. 

The following table outlines the properties available for the `TextField` component: 

|Property|Type/Values|Description|
|---|---|---|
|`label`|v0.9: String|The label for the text field.|
||v0.8:`BoundValue`||

|Property|Type/Values|Description|
|---|---|---|
|`value`(v0.9)|v0.9: String or`DataBinding`|The text content or bound path.|
|`text`(v0.8)|v0.8:`BoundValue`||
|`textFieldType`|`shortText`,`longText`,`number`,`obscured`,<br>`date`|The type of text field.|
|`validation`|String|Regular expression for|
|`Regexp`||validation.|

v0.9 JSONv0.8 JSON (#v0.8-json) (#v0.9-json) 

```
{
 "id": "email-input",
 "component": "TextField",
 "label": "Email Address",
 "value": { "path": "/user/email" },
```

- `"textFieldType": "shortText"` 

```
}
```

#### CheckBox

The `CheckBox` component is a boolean toggle that lets you switch a setting on or off. 

The following table outlines the properties available for the `CheckBox` component: 

|Propert|y Type/Values|Description|
|---|---|---|
|`label`|v0.9: String<br>v0.8:`BoundValue`|The label for the checkbox.|
|`value`|v0.9:`DataBinding`(boolean)<br>v0.8:`BoundValue`(boolean)|The value of the checkbox (true/false) or bound path.|

v0.9 JSONv0.8 JSON (#v0.8-json) (#v0.9-json) 

```
{
 "id": "terms-checkbox",
 "component": "CheckBox",
 "label": "I agree to the terms",
 "value": { "path": "/form/agreedToTerms" }
}
```

#### Slider

The `Slider` component lets you select a numeric value from a specific range. 

The following table outlines the properties available for the `Slider` component: 

|Property|Type/Values|Description|
|---|---|---|
|`value`|v0.9:`DataBinding`(number)<br>v0.8:`BoundValue`(number)|The current value of the slider or bound path.|
|`minValue`|Number|The minimum value of the range.|
|`maxValue`|Number|The maximum value of the range.|

v0.9 JSONv0.8 JSON (#v0.8-json) (#v0.9-json) `{ "id": "volume", "component": "Slider", "value": { "path": "/settings/volume" }, "minValue": 0, "maxValue": 100 }` 

#### DateTimeInput

The `DateTimeInput` component lets you pick a date and time. 

The following table outlines the properties available for the `DateTimeInput` component: 

|Property|Type/Values|Description|
|---|---|---|
|`value`|v0.9:`DataBinding`|The selected date/time value or bound path.|
||v0.8:`BoundValue`||
|`enableDate`|Boolean|Whether to enable date selection.|
|`enableTime`|Boolean|Whether to enable time selection.|

v0.9 JSONv0.8 JSON (#v0.8-json) (#v0.9-json) `{ "id": "date-picker", "component": "DateTimeInput", "value": { "path": "/booking/date" }, "enableDate": true, "enableTime": false }` 

#### ChoicePicker (v0.9) / MultipleChoice (v0.8)

Select one or more options from a list. Note that this component has been renamed into **ChoicePicker** in v0.9 from **MultipleChoice** in v0.8. 

The following table outlines the properties available: 

|Property|Type/Values|Description|
|---|---|---|
|`options`|Array of<br>Objects|The list of options selectable by the user. Each option should<br>have a label (string in v0.9, BoundValue in v0.8) and a value.|
|`selections`|v0.9:`Data`<br>`Binding`<br>v0.8:`Bound`<br>`Value`|The selected values or bound path.|

Property Type/Values Description `maxAllowed` Number The maximum number of selections allowed. `Selections` 

v0.9 JSONv0.8 JSON (#v0.8-json) (#v0.9-json) `{ "id": "country-select", "component": "ChoicePicker", "options": [ { "label": "USA", "value": "us" }, { "label": "Canada", "value": "ca" } ], "selections": { "path": "/form/country" }, "maxAllowedSelections": 1 }` 

### Basic catalog container components

Container components are used to group and organize other components. The following container components are available: 

#### Card

A `Card` component is a container with elevation, a border, and padding that groups related content. 

The following table outlines the properties available for the `Card` component: 

|Property<br>`child`|Type/Values<br>Component ID|Description<br>The ID of the component to display inside the card.|
|---|---|---|

```
{
 "id": "info-card",
 "component": "Card",
 "child": "card-content"
}
```

#### Modal

A `Modal` component is an overlay dialog triggered by an entry point component. 

The following table outlines the properties available for the `Modal` component: 

|Property|Type/Values|Description|
|---|---|---|
|`entryPoint`|Component|The ID of the component that triggers the modal (e.g., a|
|`Child`|ID|Button).|
|`contentChild`|Component<br>ID|The ID of the component to display as the content of the<br>modal.|

v0.9 JSONv0.8 JSON (#v0.8-json) (#v0.9-json) 

```
{
```

- `"id": "confirmation-modal",` 

- `"component": "Modal",` 

- `"entryPointChild": "open-modal-btn",` 

- `"contentChild": "modal-content"` 

```
}
```

#### Tabs

A `Tabs` component provides a tabbed interface for organizing content into switchable panels. 

The following table outlines the properties available for the `Tabs` component: 

Property Type/Values Description `tab` Array of The list of tabs. Each item should have a `title` (string in v0.9, `Items` Objects BoundValue in v0.8) and a `child` (component ID). 

v0.9 JSONv0.8 JSON (#v0.8-json) (#v0.9-json) `{ "id": "settings-tabs", "component": "Tabs", "tabItems": [ { "title": "General", "child": "general-tab" }, { "title": "Privacy", "child": "privacy-tab" } ] }` 

### Version differences summary

The component names and properties are largely the same across versions. The structural differences are: 

|Aspect|v0.8|v0.9|
|---|---|---|
|Component wrappe|r`"component": { "Text": { ...`|`} } "component": "Text", ...props`|
|String values|`{ "literalString": "Hello" }`|`"Hello"`|
|Children|`{ "explicitList": ["a", "b"]`|`}`<br>`["a", "b"]`|
|Data binding|`{ "path": "/data" }`|`{ "path": "/data" }`(same)|
|Text/Image styling|`usageHint`|`variant`|
|Button styling|`primary: true`|`variant: "primary"`|
|Action format|`{ "name": "..." }`|`{ "event": { "name": "..." } }`|
|Choice component|`MultipleChoice`|`ChoicePicker`|

|Aspect|v0.8|v0.9|
|---|---|---|
|Layout alignment|`distribution`,`alignment`|`justify`,`align`|
|TextField value|`text`|`value`|

### Evolution guide

For information on moving from v0.8 to v0.9, see the v0.8 to v0.9 Evolution Guide (https://a2ui.org/specification/v0.9-evolution-guide/) 

### Live examples

To see all components in action: 

```
cd samples/client/angular
yarn start gallery
```

**Note: Package Manager Usage:** Running the built-in sample applications within the A2UI repository requires Yarn ( **`yarn start gallery`** ) as configured by Corepack workspaces. For your own regular usage and standalone projects outside this repository, use the package manager of your choice (e.g. npm, pnpm). 

### What's next

**Defining Your Own Catalog** (https://a2ui.org/guides/defining-your-own-catalog/): Build your own components 

**Theming Guide** (https://a2ui.org/guides/theming/): Style components to match your brand 

Last updated 2026-10-14 UTC. 



## Add and manage A2A agents from Google Cloud Marketplace

URL: https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-marketplace-agents

**Preview** 

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the Service Specific Terms (/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the launch stage descriptions (https://cloud.google.com/products/#product-launch-stages). 

Admins can add agents from Google Cloud Marketplace that use the Agent-to-Agent (A2A) protocol. After an agent is procured (purchased) and added to Gemini Enterprise, users can access the agent through the Gemini Enterprise web app. 

**Note:** To secure agents from Cloud Marketplace, developers must configure Model Armor using the REST API within their agent's application code. The Model Armor settings in the Google Cloud console for Gemini Enterprise don't automatically protect agents registered through Cloud Marketplace. 

### Before you begin

Make sure you have the following: 

- The Gemini Enterprise Admin (/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin) role. 

- The Consumer Procurement Entitlement Viewer role 

- (/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.entitlementViewer). 

- Enabled Discovery Engine API. To enable the Discovery Engine API for your Google Cloud project, in the Google Cloud console, go to the **Discovery Engine API** page. 

Go to Discovery Engine API (https://console.cloud.google.com/apis/api/discoveryengine.googleapis.com/metrics) 

- An existing Gemini Enterprise app. To create an app, see Create an app 

- (/gemini/enterprise/docs/create-app). 

- An A2A agent registered on Cloud Marketplace. To learn how to offer AI agents in Cloud Marketplace, see Ofer AI agents through Cloud Marketplacef (/marketplace/docs/partners/ai-agents). 

**Tip:** A2A agents on Cloud Marketplace must be maintained for them to function within Gemini Enterprise. 

### Add an agent from the Cloud Marketplace to Gemini Enterprise

To add an agent from Cloud Marketplace to your Gemini Enterprise app, follow these steps: 

1. In the Google Cloud console, go to the Gemini Enterprise page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Click the name of the app to which you want to add the agent. 

3. Click **Agents > Add agent** . 

4. In the **Choose an agent type** section, click **Add** for **Agents via Marketplace** . 

5. Search for the agent you want to add, and click it. You can search by the agent's name or use semantic search to search by describing the agent's capabilities or purpose (for example, "generate reports" or "translate text"). 

6. Click **Next** . 

7. Review the agent details, then click **Next** . 

8. Enter the required authentication details, then click **Finish** . 

### Configure marketplace visibility

Admins can determine which agents from Cloud Marketplace are visible to end users in the Agent Gallery. Agent visibility is based on the agent's procurement, integration, and access status: 

Status Description 

Procured Agents that have been purchased for your organization. 

IntegratedProcured agents that an administrator has added and configured in your Gemini Enterprise app. These agents are available for users to access or request access to. 

- To configure marketplace visibility: 

   1. In the Google Cloud console, go to the Gemini Enterprise page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Click the name of the app you want to configure. 

3. Click **Agents** . 

4. Click the Settings icon to open the **Agent settings & config** panel. 

5. In the **Marketplace visibility** section, select one of the following options: 

   - **Only show accessible agents** : End users see only agents that they have access to. If there are no accessible agents, the Marketplace section is not displayed. 

   - **Only show already integrated agents** : End users see only agents that are already integrated. This includes agents that the user already has access to and agents they can 

request access to. 

   - **Only show procured agents** : (Default) End users see all procured Cloud Marketplace agents. This includes integrated agents plus agents that are not integrated yet. 

   - **Show all** : End users see all Cloud Marketplace agents, including those that they don't have access to, regardless of whether the agents are procured or integrated. 

6. Click **Done** to save your changes. 

### Set procurement contacts

You can set up contacts to receive notifications when users request access to agents that haven't been procured. These contacts receive notifications to procure the agent from Cloud Marketplace. 

To set procurement contacts: 

1. In the Google Cloud console, go to the Gemini Enterprise page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Click the name of the app you want to configure. 

3. Click **Agents** . 

4. Click the Settings icon to open the **Agent settings & config** panel. 

5. Under **Procurement contacts** , click **+ Add contact** . 

6. Enter the email address for the contact. 

7. Click **Done** to save your changes. 

### Review and approve access requests

When users request access to agents from Cloud Marketplace, you need to review and either approve or deny those requests. 

To review access requests: 

1. In the Google Cloud console, go to the Gemini Enterprise page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Click the name of the app for the agent. 

3. Click **Agents** . 

4. If the agent is already procured and integrated, you can grant access. The agents list shows **Review share request** in the row for agent with any access requests. Select **Review share request** , view the request information, and click **Grant access** to grant access. 

5. When agents require procurement or integration, a red dot on **Procurements & integration requests** indicates pending requests. Click **Procurements & integration requests** to see and manage the requests. 

Review the list of requests. The list shows the following information: 

   - **Display name** : The name of the agent. 

   - **User requests** : The number of users requesting the agent. 

   - **Status & action** : Information about procurement and integration. 

- The list shows agent access requests where the agent is not yet procured or not yet integrated. 

   - If the agent is not procured, it must be procured as the next step. If the procurement contact (#set-procurement-contacts) for the agent is set, a note indicates that a procurement request was sent to the contact. If the procurement contact for the agent is not set, you are prompted to add a procurement contact. 

   - Once the agent is procured, you can click **Integrate & grant access** to complete integration. Once integration is complete you can give users access. 

### Delete an agent from Gemini Enterprise

To delete an agent from your Gemini Enterprise app, follow these steps: 

1. In the Google Cloud console, go to the Gemini Enterprise page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Click the name of the app that the agent is registered with. 

3. Click **Agents** . 

4. Click the icon next to the agent you want to delete. 

5. Click **Delete** . 

Last updated 2026-10-14 UTC. 



## Import A2A agents from Agent Registry

URL: https://docs.cloud.google.com/gemini/enterprise/docs/import-govern-agent-registry

As an administrator of Gemini Enterprise, you can add an A2A agent from Agent Registry to a Gemini Enterprise app. 

You can apply access control policies to traffic through Agent Gateway. These policies let you enforce egress governance to control traffic to agents. 

### About A2A agents and Agent Registry

Agent2Agent (A2A) Protocol (https://a2a-protocol.org/) is an open communication protocol and a universal language for agents. The protocol enables agents from different builders and platforms to discover each other, collaborate, and securely delegate tasks. 

Agent Registry (/agent-registry/overview) is a centralized, queryable catalog that acts as the single source of truth for discovering, tracking, and managing A2A agents, endpoints, and MCP servers. 

The A2A agents in the registry can be custom agents built by you and your colleagues and deployed on various runtimes such as Agent Runtime on Gemini Enterprise Agent Platform, Cloud Run or Google Kubernetes Engine (GKE). These agents can also be agents built in our Google products, such as Google Workspace. 

You can associate the agents in Agent Registry with your Gemini Enterprise apps to make them available to the app's end users. 

### About Agent Gateway

Agent Gateway is the managed regional networking component of Agent Platform that acts as the traffic controller and runtime policy enforcement point for A2A agents, MCP servers, and endpoints. It secures and governs connectivity: between 

clients and A2A agents; A2A agents and backend tools; or A2A agents and other agents. 

Before you can associate A2A agents with your Gemini Enterprise apps, you need to have set up an Agent Gateway through which agent traffic can be routed. See Before you begin (#prerequisites) below. 

### Regional constraints for the registry, gateway, and app

To ensure compliance with data residency requirements, both Agent Registry and Agent Gateway resources are project-and-region-specific. 

A Agent Gateway must be configured to associate with a Agent Registry that is in a region compatible with the Gemini Enterprise app's operational region. This prevents violations of data residency conventions. For example, a Gemini Enterprise app created in the US region must use an Agent Gateway configured with a US-regional Agent Registry, not a global one. 

For Gemini Enterprise apps, the regional alignment is strictly enforced through a specific binding process: 

- The Gemini Enterprise app must bind only to an Agent Gateway located within one of the allowed regions for that app. 

- The selected Agent Gateway must be associated with an Agent Registry. This Agent Registry must also be located in the same specific region as the Agent Gateway and the app. 

- This means the three components (app, gateway, and registry) must be regionally aligned. The table below provides the specific region mappings: 

|Gemini Enterprise app location|Agent Gateway location|Agent Registry location|
|---|---|---|
|`global`|`us-central1`|`us-central1`,`us`, or`global`|
|`us`|`us-central1`|`us-central1`or`us`|
|`eu`|`europe-west1`|`europe-west1`or`eu`|

### Limitations

The following limitations apply when you import agents from Agent Registry: 

- You can only discover and import agents from Agent Registry if the registry is associated with the Agent Gateway set up for your Gemini Enterprise app. 

- You can apply governance policies only to agents residing within the single registry associated with the Agent Gateway. 

- Direct communication between Gemini Enterprise agents, or between a Gemini Enterprise agent and a Gemini Enterprise data connector (including MCP-based connectors such as the custom MCP server) doesn't trigger Agent Gateway policy enforcement. 

### Before you begin

Before you begin, make sure you've completed the following prerequisites: 

- You have the Gemini Enterprise Admin 

- (/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin) role. 

- You've set up a gateway to route agent traffic through Agent Gateway. For more information, see Route Gemini Enterprise traffic through Agent Gateway (/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-ge-deploy). 

### Import agents from Agent Registry to a Gemini Enterprise app

Importing an A2A agent from Agent Registry into your Gemini Enterprise app lets you make the agent available to the app's end users. 

**Important:** When you configure, and allow your End Users to access, an agent imported from Agent Registry, their query string — which may be rewritten based on prior conversation context — and tool parameters may be sent to the agent (and to any tools or MCP servers the agent invokes), and those systems may be able to link this data with their 

identity. Data in such systems is subject to the agent provider's Terms of Service and Privacy Policy. 

Console 

(#console) 

To import an agent from Agent Registry to a Gemini Enterprise app, do the following: 

1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

   - Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Click the name of the app that you want to associate an A2A agent with. 

3. Click **Agents** . 

4. Click **+ Add agent** , and click **Add** for **Custom agent via Agent Runtime** . 

5. Find the agent that you want to add, and click **Add agent** . 

6. Review the agent details, and click **Next** . 

7. Do one of the following: 

      - If the agent is publicly available or if permission for a runtime already exists, click **Skip & Finish** . 

      - Otherwise, review or enter the **Provider credentials** and **Additional details** , and click **Finish** . 

|Field|Description|
|---|---|
|Client ID|The unique identifier of the OAuth application that you<br>registered with your identity provider to represent Gemini<br>Enterprise.|
|Client secret|The confidential key associated with the OAuth application<br>that you registered with your identity provider to represent<br>Gemini Enterprise.|

Field Description Authorization The URL that users use to authorize Gemini Enterprise to URL access the agent. For example, `https://accounts.google. com/o/oauth2/v2/auth?client_id=123...abc.apps. googleusercontent&redirect_ uri=https%3A%2F%2Fvertexaisearch.cloud.google. com%2Foauth-redirect&oauth-redirect&include_ granted_scopes=true&response_type=code&access_ type=offline&prompt=consent` . Note: Make sure that your OAuth app has this redirect URI: **`https://vertexaisearch.cloud.google.com/oauthredirect`** 

Token URL The endpoint used to exchange the authorization code for an access token. For example, if the agent is hosted by Google, the token URL is `https://oauth2.googleapis.com/token` . Scopes The permissions that define what actions Gemini Enterprise can perform on behalf of a user, or what data it can access. Gemini Enterprise requests these scopes during user authorization. For example, `https://www.googleapis.com/ auth/cloud-platform` . 

When you specify scopes, consider the following: 

Provide a space-separated list of scopes. For example: `read write` . Ensure the scopes are sufficient to let the user sign in and use the agent. 

PKCE Select this if Proof Key for Code Exchange is required by the verification agent. enabled 

8. To make the agent available to the app's end users, do the following: 

   - a. Navigate to the **User permissions** tab for the agent: **Apps** > _APP_NAME_ > **Agents** > _AGENT_NAME_ > **User permissions** . 

   - b. Click **Add user** . 

c. In the **Add user permissions roles to agent** dialog, assign the **Agent User** role to a user, a group, or all users. 

### Set up and apply egress governance policies

Using Agent Gateway, you can assess and apply semantic and IAM control policies (/gemini-enterprise-agent-platform/govern/policies/overview) to egress agent traffic. You can create granular egress policies to manage agent-to-agent access for your A2A agents. 

You define allow and deny rules restricting an agent's access to specific entries within Agent Registry. 

To create and apply egress governance rules to agents, do one of the following: 

- Create IAM agent policies 

- (/gemini-enterprise-agent-platform/govern/policies/assign-identity-iam) 

- Configure semantic governance policies 

- (/gemini-enterprise-agent-platform/govern/policies/configure-semantic-governance) 

### What's next

Test the agent (/gemini/enterprise/docs/agents-overview#manage_agents) 

Last updated 2026-10-14 UTC.
